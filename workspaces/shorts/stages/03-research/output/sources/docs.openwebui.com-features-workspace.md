# Workspace / Open WebUI

- Source URL: https://docs.openwebui.com/features/workspace/
- Accessed: 2026-11-25
- Fetched via: web_extract
- Tier: docs

## Page text (copied from the fetch result)

[Skip to main content](https://docs.openwebui.com/features/workspace/#__docusaurus_skipToContent_fallback)

On this page

![Workspace: an organizer tray with one compartment filled](https://docs.openwebui.com/images/banners/workspace-light.svg)

**Compose your own AI from five building blocks.**

The Workspace is where you turn a raw model into something tailored to your work. Bind knowledge, attach tools, set a system prompt, teach it skills and save the result as a reusable model. Every piece is optional and they stack: a model with your handbook attached, your house style as a prompt and the right tools wired in.

| Building block | What it is for |
| --- | --- |
| [**Models**](https://docs.openwebui.com/features/workspace/models) | Wrap a base model with a system prompt, parameters, knowledge and tools, then save it as a reusable preset in the model picker. |
| [**Knowledge**](https://docs.openwebui.com/features/workspace/knowledge) | Upload documents and build knowledge bases the AI retrieves from (RAG), so it answers from your sources instead of guessing. |
| [**Prompts**](https://docs.openwebui.com/features/workspace/prompts) | Save reusable prompt templates with typed variables, callable in any chat with a `/` slash command. |
| [**Skills**](https://docs.openwebui.com/features/workspace/skills) | Markdown instruction sets that teach a model how to approach a task (methodology, steps, house rules), with optional [supporting files](https://docs.openwebui.com/features/workspace/skills#supporting-files), loaded on demand. |
| [**Tools** ↗](https://docs.openwebui.com/features/extensibility/plugin/tools) | Give models real abilities they can call: APIs, code, the web. Tools are documented under [**Plugins & Extensibility**](https://docs.openwebui.com/features/extensibility/plugin/tools), not here. |

Each has its own page, so start anywhere. Most people begin with a custom **Model** and add the other pieces as they need them.

Sorting the lists

The **Models**, **Knowledge**, **Prompts**, **Skills** and **Tools** lists, along with **Notes** and the admin **Functions** list, can be ordered by clicking the **Title** or **Updated at** column heading. Clicking the heading you are already sorted by reverses the direction. Each list opens on **Updated at**, newest first.

Profile cards

Pointing at an owner's name in the **Models**, **Knowledge**, **Prompts**, **Skills** and **Tools** lists or the admin **Functions** list, at the author of a version in the version history or at a person in an item's access settings opens their profile card, the same one [channels](https://docs.openwebui.com/features/channels) show. It has their name, status, bio, groups, local time and when they were last active.

With [comments](https://docs.openwebui.com/features/chat-conversations/chat-features/comments) turned on, each item in these lists can be discussed in a side panel.

## Workspace access and sharing [​](https://docs.openwebui.com/features/workspace/\#workspace-access-and-sharing "Direct link to Workspace access and sharing")

Workspace is a section of your Open WebUI instance. To collaborate, share individual items such as a skill or knowledge base with the people or groups who need them.

Each tab has its own [Workspace permission](https://docs.openwebui.com/features/authentication-access/rbac/permissions#1-workspace-permissions). If you cannot open a tab, ask an administrator to check **Admin Panel > Users > Groups > Default Permissions** and the permissions of your groups. For example, **Workspace > Skills Access** opens the **Skills** tab. The built-in defaults for these tab permissions are off for non-admins. The **Tools** tab also requires Tools to be enabled on the instance.

To share a skill you can edit, open it in **Workspace > Skills**, click **Access**, and use **Add Access** to choose an eligible user or group. The **Access** button requires **Sharing > Skills Sharing** for non-admins, which is off by default. The recipient's access to the skill and their permission to open the **Skills** tab are checked separately.

## Creating, importing and exporting [​](https://docs.openwebui.com/features/workspace/\#creating-importing-and-exporting "Direct link to Creating, importing and exporting")

Everything that adds or moves workspace items runs through one **Create** button, at the right of the Workspace header next to the section tabs. The individual pages do not carry their own **\+ New Model**, **\+ New Prompt** or similar buttons. The button acts on the section you are currently looking at, and the chevron beside it opens the rest of that section's actions (the menu repeats **Create** as its first entry).

| Section | Create | Also in the menu |
| --- | --- |
| **Models** | Opens the model editor on its own page | Import JSON, Export JSON |
| **Knowledge** | Opens a dialog on top of the list | none |
| **Prompts** | Opens a dialog on top of the list | Import JSON, Export JSON |
| **Skills** | Opens the skill editor on its own page | Import, Import from URL (admins only), Import folder, Export ZIP, Export JSON |
| **Tools** | Opens the tool editor on its own page | Import from URL (admins only), Import JSON, Export JSON |

When a section has only one action available, the chevron is dropped and **Create** is a plain button. That is always the case for Knowledge, and it happens elsewhere when the import and export permissions are withheld: each menu entry is gated by the matching `workspace` permission (`models_import`, `prompts_export` and so on), and admins always see all of them. Export writes the section's items to a JSON file (Skills also to a ZIP), which the matching Import reads back.

The old create URLs still resolve. `/workspace/prompts/create` and `/workspace/knowledge/create` open the list with the create dialog already open, and closing it returns you to the list.

This content is for informational purposes only and does not constitute a warranty, guarantee, or contractual commitment. Open WebUI is provided "as is." See your [license](https://docs.openwebui.com/license) for applicable terms.

- [Workspace access and sharing](https://docs.openwebui.com/features/workspace/#workspace-access-and-sharing)
- [Creating, importing and exporting](https://docs.openwebui.com/features/workspace/#creating-importing-and-exporting)

Analytics preferences
