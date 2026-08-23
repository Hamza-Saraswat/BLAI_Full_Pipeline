# Signature Analogies

The channel's recurring pictures. A feed viewer meets us cold every time, so these ideas get re-taught often and that is correct. What must not repeat is the wording: re-teach the same picture in fresh sentences, at the length this video can afford.

Use one analogy per script at most. If none of these fits, prefer the plain mechanism over inventing a new picture; a new vehicle is a decision worth making deliberately, and it goes in this file once it has been used twice.

## The doorway

- **Vehicle:** a kitchen where the chef chops instantly, but every ingredient arrives through one narrow doorway.
- **Maps to:** memory bandwidth. The chef is compute, the doorway is the memory bus, the ingredients are the model's weights.
- **The point:** to write one word the machine reads the model's active weights out of memory. Not think. Read.
- **Limit:** it breaks for prompt processing, which reads the whole prompt in one wide pass rather than one word at a time. Say "reading your prompt is one big block of math" instead of stretching the kitchen.
- **Shortest usable form:** "Your GPU isn't slow. Its doorway is."

## The receptionist

- **Vehicle:** a company of a hundred specialists with a receptionist at the front desk who wakes only the few you need.
- **Maps to:** a mixture of experts. The specialists are experts, the receptionist is the router.
- **The point:** speed comes from the few that wake; memory comes from all of them, because any of them could be next.
- **Limit:** the router re-picks for every word, so it is not one hand-off but hundreds. Do not let the picture imply a single decision per question.
- **Shortest usable form:** "One hundred twenty billion parameters. Five billion wake up per word."

## The desk

- **Vehicle:** one shared room, one brain, and a separate desk for each person in the house.
- **Maps to:** a KV cache per session. The room is the loaded model, the desk is one conversation's running notes.
- **The point:** the model is loaded once and shared; the context is private and grows with every word.
- **Limit:** desks are not free and they do not shrink. The picture must not suggest the room is the only cost.
- **Shortest usable form:** "One brain, three laptops, three desks."

## Rounding pi

- **Vehicle:** pi written out to five places, then rounded to three point one.
- **Maps to:** quantization. Each stored number keeps fewer bits.
- **The point:** most of the accuracy survives, and the file gets dramatically smaller.
- **Limit:** the loss is not uniform. Exact math notices first; casual chat never does. Say which one this video is about.
- **Shortest usable form:** "Seventy percent smaller. Barely dumber."

## Rules

1. One analogy per script. Two pictures for one idea is worse than none, and the evidence on seductive detail is against you.
2. Every analogy states its limit somewhere in the script, in one clause. A picture without a limit is a claim we cannot defend.
3. Never re-use a sentence from an earlier script. The variety check flags any eight-word run that appears in the last ten scripts.
4. The vehicle can repeat; the words cannot. That is the whole policy.
