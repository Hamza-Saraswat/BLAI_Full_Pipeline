#!/usr/bin/env python3
"""pick_slot must never abort a publish because of a badly formatted publish_slot_hint.

Regression for 2026-09-16: the package agent wrote "11:00 CT" into publish_slot_hint and
publish.py exited 1 ("not an ISO-8601 timestamp") before talking to Blotato. A hint is a
hint: an unreadable one is logged and ignored, and the next free slot is used instead.

  python3 skills/blotato-publish/tests/test_pick_slot.py
Stdlib only, no network, no repo writes.
"""
from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import sys
import unittest

SCRIPTS = pathlib.Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))
import publish  # noqa: E402

NOW = dt.datetime(2026, 9, 16, 17, 8, 46, tzinfo=dt.timezone.utc)  # 12:08 CDT, the real approval time


def args_auto() -> argparse.Namespace:
    return argparse.Namespace(slot="auto")


class PickSlotHint(unittest.TestCase):
    def setUp(self):
        self._taken = publish.taken_slots
        publish.taken_slots = lambda own_slug: []  # no hub-note scan; keep the test hermetic

    def tearDown(self):
        publish.taken_slots = self._taken

    def test_prose_hint_falls_through_to_next_free_slot(self):
        manifest = {"slug": "x", "format": "short", "publish_slot_hint": "11:00 CT"}
        self.assertEqual(publish.pick_slot(args_auto(), manifest, NOW), "2026-09-16T18:00:00-05:00")

    def test_future_iso_hint_is_honoured(self):
        manifest = {"slug": "x", "format": "short", "publish_slot_hint": "2026-09-17T11:00:00-05:00"}
        self.assertEqual(publish.pick_slot(args_auto(), manifest, NOW), "2026-09-17T11:00:00-05:00")

    def test_past_iso_hint_falls_through(self):
        manifest = {"slug": "x", "format": "short", "publish_slot_hint": "2026-09-16T11:00:00-05:00"}
        self.assertEqual(publish.pick_slot(args_auto(), manifest, NOW), "2026-09-16T18:00:00-05:00")


if __name__ == "__main__":
    unittest.main()
