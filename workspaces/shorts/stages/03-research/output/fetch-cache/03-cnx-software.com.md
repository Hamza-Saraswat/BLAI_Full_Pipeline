<!-- url: https://www.cnx-software.com/2026/10/19/axera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost/ -->
<!-- fetched via web_extract 2026-10-24, tier 2 (docs). By Jean-Luc Aufranc (CNXSoft), 2026-10-19. -->

Axera AX8860P 16-core Cortex-A55 SoC takes on NVIDIA DGX Spark at fraction of the cost - CNX Software

[Skip to content](https://www.cnx-software.com/2026/10/19/axera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost/#content)

Axera AX8860P is a new 16-core Cortex-A55 SoC with up to 128 TOPS/256 TOPS (FP4) NPU, 256-bit LPDDR5/5X memory, and PCIe 5.0 connectivity, aiming to power desktop AI solutions competing with [NVIDIA DGX Spark](https://www.cnx-software.com/2025/03/19/nvidia-dgx-spark-a-desktop-ai-supercomputer-powered-by-nvidia-gb10-20-core-armv9-soc-with-1000-tops-of-ai-performance/) at a fraction of the cost.

Dr. Qiu Xiaoxin, founder and CEO of Axera, unveiled the new AX8860/AX8860P processor a few days ago at the China International Industrial Fair, along with upcoming products from Sipeed and Radxa.

[![Axera AX8860 products](https://www.cnx-software.com/wp-content/uploads/2026/10/Axera-AX8860-products-720x654.jpg)](https://www.cnx-software.com/wp-content/uploads/2026/10/Axera-AX8860-products.jpg)

Axera AX8860P key features and specifications:

- CPU – 16x Arm Cortex-A55 processor
- AI – Up to 256 TOPS
- VPU – 64-channel decode, 16-channel encode
- Memory – Up to 128GB 256-bit LPDDR5x with 273GB/s bandwidth
- Interconnect – PCIe 5.0 + AXLink (C2C) cascading with 80% efficiency for multi-chip cards and systems
- Power Consumption – About 40 Watts under load
- Package – 78 × 78 mm module
- Process – 6nm

![Axera AX8860P key features](https://www.cnx-software.com/wp-content/uploads/2026/10/Axera-AX8860P-key-features.webp)

The AX8860P SoC is said to support vLLM, SGLang, PyTorch, ONNX, Hugging Face formats, OpenAI-compatible APIs, and Axera’s toolchain. [Some documentation](https://pulsar2-docs.readthedocs.io/en/latest/user_guides_quick/quick_start_ax8860.html) is already available showing how to convert a MobileNetV2 ONNX model into an “axmodel” running on the Axera chip.

In terms of hardware, [Radxa will introduce](https://x.com/RadxaComputer/status/2109917923678846976/photo/1) a “Pocket Supercomputer” powered by the AX8860P SoC, but has yet to provide details since it’s still a few months away.

![Radxa Pocket Supercomputer](https://www.cnx-software.com/wp-content/uploads/2026/10/Radxa-Pocket-Supercomputer.webp) Radxa Pocket Supercomputer

Sipeed also has a few AX8860P PCIe cards on the way (with up to four chips with the MaixBlade), and a MaixStation mini AI computer for which we have more details, and you can even reserve one.

MaixStation specifications:

- SoC – Axera AX8860P described above
- System Memory – 32GB or 128GB LPDDR5x
- Host interface
  - USB 3.0 Type-C port connected to a laptop
  - 10GbE SFP+ cage connected to the local network
- Misc
  - Power button
  - Ethernet/USB-C mode switch
- Power Supply – 65W USB PD via USB Type-C port
- Power Consumption – 40W typical
- Dimensions – 110 x 110 x 30 mm

![Sipeed Maixstation vs Mac Mini vs DGX Spark](https://www.cnx-software.com/wp-content/uploads/2026/10/Sipeed-Maixstation-vs-Mac-Mini-vs-DGX-Spark.webp) Sipeed MaixStation vs Mac Mini vs DGX Spark![Sipeed Maixstation ports](https://www.cnx-software.com/wp-content/uploads/2026/10/Sipeed-Maixstation-ports.webp) Sipeed MaixStation ports

A single 32GB node can run Qwen3.8‑27B, a single 128GB node supports Qwen3.8‑Flash‑Next 125B, a dual node with 256 GB RAM can handle DeepSeek V4‑Flash 284B, and a quad-node (Maixstation Pro) with 512GB manages DeepSeek V4.1‑Flash 552B.

Sipeed also shared Qwen benchmarks comparing the MaixStation 128GB to the DGX Spark 128GB. The numbers show it’s only slightly faster, but they expect further optimization will widen the gap.

![Axera AX8860P vs DGX Spark benchmarks](https://www.cnx-software.com/wp-content/uploads/2026/10/Axera-AX8860P-vs-DGX-Spark-benchmarks.webp)

The company explains that “256 TOPS” beats the “1,000 TOPS” advertised by NVIDIA because the latter is sparse FP4, which real models can’t use, while Dense is around 500 on paper, but Spark only puts a small slice of it to work, while MaixStation makes better use of its 256 TOPS.

The bandwidth is the same for both systems at 273 GB/s, but Axera AX8860P is said to implement architecture improvements to “keep more of those 273 GB/s busy”. Finally, MTP (speculative decoding) is turned off in the benchmarks above for side-by-side comparison.

![Sipeed MaixStation vs DGX Spark front](https://www.cnx-software.com/wp-content/uploads/2026/10/Sipeed-MaixStation-vs-DGX-Spark-front.webp) Sipeed MaixStation vs DGX Spark

The NVIDIA DGX Spark was first unveiled in March 2025 for $3,000 to $4,000, but since then, price increases have kicked in, and it sells now for $6,949.99. While the MaixStation is not for sale now, the company says the 32GB model will go for under $2000 and the 128GB model for under $4000, let’s make that $3,999… Daisy-chaining more than two systems is also much cheaper on the MaixStation since you only need a cable, but a $4000 200G/400G switch for the NVIDIA systems.

Sipeed will launch it on Kickstarter in a few months and invites users to pay a $30 reservation fee to get 100 off once the crowdfunding campaign starts. You’ll find more technical details and the reservation link on [the product page](https://sipeed.com/maixstation/index.html).

![Jean Luc Aufranc](https://www.cnx-software.com/wp-content/uploads/2023/05/Jean-Luc-Aufranc.webp)

[Jean-Luc Aufranc (CNXSoft)](https://www.cnx-software.com/author/cnxsoft/)

Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.

[Twitter](https://www.twitter.com/cnxsoft "Twitter")[Linkedin](https://www.linkedin.com/in/cnxsoft/ "Linkedin")

Share this:

[Facebook](https://www.cnx-software.com/#facebook "Facebook") [Twitter](https://www.cnx-software.com/#twitter "Twitter") [Hacker News](https://www.cnx-software.com/#hacker_news "Hacker News") [Slashdot](https://www.cnx-software.com/#slashdot "Slashdot") [Reddit](https://www.cnx-software.com/#reddit "Reddit") [LinkedIn](https://www.cnx-software.com/#linkedin "LinkedIn") [Pinterest](https://www.cnx-software.com/#pinterest "Pinterest") [Flipboard](https://www.cnx-software.com/#flipboard "Flipboard") [MeWe](https://www.cnx-software.com/#mewe "MeWe") [Line](https://www.cnx-software.com/#line "Line") [Email](https://www.cnx-software.com/#email "Email") [Share](https://www.addtoany.com/share#url=https%3A%2F%2Fwww.cnx-software.com%2F2026%2F10%2F19%2Faxera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost%2F&title=Axera%20AX8860P%2016-core%20Cortex-A55%20SoC%20takes%20on%20NVIDIA%20DGX%20Spark%20at%20fraction%20of%20the%20cost)

**Support CNX Software! Donate via [cryptocurrencies](https://www.cnx-software.com/donate-cryptocurrencies/), [become a Patron](https://www.patreon.com/cnxsoft) on Patreon, or purchase goods on [Amazon](https://amzn.to/3SXubZ0) or [Aliexpress](https://s.click.aliexpress.com/e/_DmGIIRT)**. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.

[![Radxa Dragon Q8B Edge AI SBC with Snapdragon 8cx Gen3 SoC](https://www.cnx-software.com/wp-content/uploads/2026/06/Radxa-Dragon-Q8A-sbc.webp)](https://arace.tech/products/radxa-dragon-q8b)

Subscribe

[Login](https://www.cnx-software.com/smart-login/?redirect_to=https%3A%2F%2Fwww.cnx-software.com%2F2026%2F10%2F19%2Faxera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost%2F)

Notify of

new follow-up commentsnew replies to my comments

Connect with:

[![Facebook](https://www.cnx-software.com/wp-content/plugins/wordpress-social-login/assets/img/32x32/wpzoom//facebook.png)](https://www.cnx-software.com/smart-login/?action=wordpress_social_authenticate&mode=login&provider=Facebook&redirect_to=https%3A%2F%2Fwww.cnx-software.com%2F2026%2F10%2F19%2Faxera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost%2F "Connect with Facebook")[![Google](https://www.cnx-software.com/wp-content/plugins/wordpress-social-login/assets/img/32x32/wpzoom//google.png)](https://www.cnx-software.com/smart-login/?action=wordpress_social_authenticate&mode=login&provider=Google&redirect_to=https%3A%2F%2Fwww.cnx-software.com%2F2026%2F10%2F19%2Faxera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost%2F "Connect with Google")[![Twitter](https://www.cnx-software.com/wp-content/plugins/wordpress-social-login/assets/img/32x32/wpzoom//twitter.png)](https://www.cnx-software.com/smart-login/?action=wordpress_social_authenticate&mode=login&provider=Twitter&redirect_to=https%3A%2F%2Fwww.cnx-software.com%2F2026%2F10%2F19%2Faxera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost%2F "Connect with Twitter")

![guest](https://gravatar.webp.se/avatar/52ae47676688610fa720cada2fc0b36f583611cc0e11511fb6050b4c72c07bd8?s=112&d=mm&r=g)

Label

{}\[+\]

Name\*

Email\*

Website

I agree to the [Privacy Policy](https://www.cnx-software.com/privacy-policy)

The comment form collects your name, email and content to allow us keep track of the comments placed on the website. Please read and accept our website Terms and Privacy Policy to post a comment.

Connect with:

[![Facebook](https://www.cnx-software.com/wp-content/plugins/wordpress-social-login/assets/img/32x32/wpzoom//facebook.png)](https://www.cnx-software.com/smart-login/?action=wordpress_social_authenticate&mode=login&provider=Facebook&redirect_to=https%3A%2F%2Fwww.cnx-software.com%2F2026%2F10%2F19%2Faxera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost%2F "Connect with Facebook")[![Google](https://www.cnx-software.com/wp-content/plugins/wordpress-social-login/assets/img/32x32/wpzoom//google.png)](https://www.cnx-software.com/smart-login/?action=wordpress_social_authenticate&mode=login&provider=Google&redirect_to=https%3A%2F%2Fwww.cnx-software.com%2F2026%2F10%2F19%2Faxera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost%2F "Connect with Google")[![Twitter](https://www.cnx-software.com/wp-content/plugins/wordpress-social-login/assets/img/32x32/wpzoom//twitter.png)](https://www.cnx-software.com/smart-login/?action=wordpress_social_authenticate&mode=login&provider=Twitter&redirect_to=https%3A%2F%2Fwww.cnx-software.com%2F2026%2F10%2F19%2Faxera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost%2F "Connect with Twitter")

![guest](https://gravatar.webp.se/avatar/778929b2fea62a88f6d2ffa50e2d23b11922702f1a0b13a621b60af308959c47?s=112&d=mm&r=g)

Label

{}\[+\]

Name\*

Email\*

Website

I agree to the [Privacy Policy](https://www.cnx-software.com/privacy-policy)

The comment form collects your name, email and content to allow us keep track of the comments placed on the website. Please read and accept our website Terms and Privacy Policy to post a comment.

14 Comments

oldest

newest

![Andy Lin](https://gravatar.webp.se/avatar/bc3a1e9b0cb049da08595702bc7f5fe3b1bbb34f277343f92a2db193a0fc7e52?s=128&d=mm&r=g)

Andy Lin

5 days ago

[Share On Twitter](https://x.com/intent/post?text=&url=https%3A%2F%2Fwww.cnx-software.com%2F2026%2F10%2F19%2Faxera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost%2F%23comment-662699 "Share On Twitter")

Uh there are huge difference in CPU: ?GHz 12x a55 vs 10x < 3.9GHz x925 + 10x <2.6GHz x725, and 128/256GOPS vs 1POPS in FP4.

Reply

![zepan](https://gravatar.webp.se/avatar/f4be22d8eadc263cdb3dd70998b34ac9fe4268e86dfba6a84242d50dd4b95bc3?s=128&d=mm&r=g)

zepan

4 days ago

[Share On Twitter](https://x.com/intent/post?text=&url=https%3A%2F%2Fwww.cnx-software.com%2F2026%2F10%2F19%2Faxera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost%2F%23comment-662711 "Share On Twitter")

[Andy Lin](https://www.cnx-software.com/2026/10/19/axera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost/#comment-662699)

Don’t believe NVIDIA’s “1POPS”, that even slower than 200T

Reply

![Hedda](https://gravatar.webp.se/avatar/977859ee15613356a8a5297f7763e0576b1d019b3e48030d109831dad664a1a5?s=128&d=mm&r=g)

Hedda

5 days ago

[Share On Twitter](https://x.com/intent/post?text=&url=https%3A%2F%2Fwww.cnx-software.com%2F2026%2F10%2F19%2Faxera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost%2F%23comment-662703 "Share On Twitter")

They should make a DDR4 variant so could have a lower cost variant with as much unified memory

.

Reply

![Willy](https://gravatar.webp.se/avatar/e3728bb535d8309361a2e541df14e3383d9e946cf97417a14e0ae3bbed09daf0?s=128&d=mm&r=g)

[Willy](https://wtarreau.blogspot.com/)

4 days ago

[Share On Twitter](https://x.com/intent/post?text=&url=https%3A%2F%2Fwww.cnx-software.com%2F2026%2F10%2F19%2Faxera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost%2F%23comment-662710 "Share On Twitter")

[Hedda](https://www.cnx-software.com/2026/10/19/axera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost/#comment-662703)

Exactly. Let’s just have 512 (8-ch) or 1024-bit (16-ch) DDR4 and beat all expensive stuff.

Reply

![Michael Jordan](https://gravatar.webp.se/avatar/f0e126f6446bf778b42547abf7fbaae0be992d5125e21382a9db8662d6ede6b1?s=128&d=mm&r=g)

Michael Jordan

4 days ago

[Share On Twitter](https://x.com/intent/post?text=&url=https%3A%2F%2Fwww.cnx-software.com%2F2026%2F10%2F19%2Faxera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost%2F%23comment-662717 "Share On Twitter")

They went cheap with the 10Gb interconnect. That’s going to be the bottleneck. May be great for 1 box.

Reply

![Tuff_Pro](https://gravatar.webp.se/avatar/9f9231fab3fdc42815a46a58e7ccafb9df3493764a57f24fafb67ee69b6b14cd?s=128&d=mm&r=g)

Tuff\_Pro

4 days ago

[Share On Twitter](https://x.com/intent/post?text=&url=https%3A%2F%2Fwww.cnx-software.com%2F2026%2F10%2F19%2Faxera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost%2F%23comment-662724 "Share On Twitter")

So i could just plug this in my PC and run LLMs with?

Reply

![Bob](https://gravatar.webp.se/avatar/481e120c25a6b2ea4dd6879c12ec8e10012e0508d033a1ff41de1a5b26118bfc?s=128&d=mm&r=g)

Bob

4 days ago

[Share On Twitter](https://x.com/intent/post?text=&url=https%3A%2F%2Fwww.cnx-software.com%2F2026%2F10%2F19%2Faxera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost%2F%23comment-662731 "Share On Twitter")

[Tuff\_Pro](https://www.cnx-software.com/2026/10/19/axera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost/#comment-662724)

This is a PC

Reply

[![Jean-Luc Aufranc (CNXSoft)](https://www.cnx-software.com/wp-content/uploads/2023/05/Jean-Luc-Aufranc.webp)](https://www.cnx-software.com/author/cnxsoft/)

Author

[Jean-Luc Aufranc (CNXSoft)](https://www.cnx-software.com/author/cnxsoft/)

4 days ago

[Share On Twitter](https://x.com/intent/post?text=&url=https%3A%2F%2Fwww.cnx-software.com%2F2026%2F10%2F19%2Faxera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost%2F%23comment-662733 "Share On Twitter")

[Bob](https://www.cnx-software.com/2026/10/19/axera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost/#comment-662731)

It will probably be a poor PC, it’s better seen as an AI box attached via USB to a host or a local network.

Reply

![David Jashi](https://lh3.googleusercontent.com/a/ACg8ocIsQ8Z43mpjhNcHA40cqX2hKwxV18hC0Ck55GSOFcBvc5Jmgg2Ogg=s96-c)

David Jashi

2 days ago

[Share On Twitter](https://x.com/intent/post?text=&url=https%3A%2F%2Fwww.cnx-software.com%2F2026%2F10%2F19%2Faxera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost%2F%23comment-662804 "Share On Twitter")

[Jean-Luc Aufranc (CNXSoft)](https://www.cnx-software.com/2026/10/19/axera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost/#comment-662733)

I feel more interested in “AX8860P PCIe card”, actually. I wonder if they will be able to shove all 128GB in each of them and how wide will it be. Would be nice to have 4 of them in 1RU server with 512GB total per RU. 160W shouldn’t be a problem neither from power supply nor from heat dissipation point of view.

Reply

![Meierz](https://gravatar.webp.se/avatar/7e35797a0d4bf7ff46e880b912877bc0053e604f0c333f3e62d51c6a38c93840?s=128&d=mm&r=g)

Meierz

4 days ago

[Share On Twitter](https://x.com/intent/post?text=&url=https%3A%2F%2Fwww.cnx-software.com%2F2026%2F10%2F19%2Faxera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost%2F%23comment-662725 "Share On Twitter")

No signs of any dedicated GPU. Should have added even a cheap Vivante GC7000L to allow stand-alone use as a general desktop, because being able to carry around a low-power 16 core mini in your pants pocket for non-AI tasks would be a great selling point. Also if they want buyers, they are going to need to go beyond the SDK and prioritize their opensource plan. So ahead of launch, get those drivers for hardware and npu to mainline linux kernel and mesa vulkan working ASAP in order to differentiate their product to better compete with Nvidia’s proprietary junk. That… Read more »

Reply

![Antonym](https://gravatar.webp.se/avatar/4cd85759387b6196d7d6167241e22885d1bb1574f06d8ec8b07b5a9c1e8a888e?s=128&d=mm&r=g)

Antonym

4 days ago

[Share On Twitter](https://x.com/intent/post?text=&url=https%3A%2F%2Fwww.cnx-software.com%2F2026%2F10%2F19%2Faxera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost%2F%23comment-662736 "Share On Twitter")

Why desktop AI in a small (plastic) box? What is wrong with a bigger aluminum housing?

40W only means less AI power: hype product.

Speed between processors and memory is vital.

Reply

![Hussam](https://gravatar.webp.se/avatar/97d2c858aa89d6cb3d3e9dc5927c00e705d97692c281f579c4dc1febb169349b?s=128&d=mm&r=g)

[Hussam](http://hertaville.com/)

3 days ago

[Share On Twitter](https://x.com/intent/post?text=&url=https%3A%2F%2Fwww.cnx-software.com%2F2026%2F10%2F19%2Faxera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost%2F%23comment-662756 "Share On Twitter")

Massively underpowered CPU. For this kind of dough, the least they can do is place 4-8 cortex-A76/8s cores. .

Reply

![kcg](https://gravatar.webp.se/avatar/b576923c78f58bb02fbe0de9b7f869b6f6b012a3ecb7931fd3f143097e75087c?s=128&d=mm&r=g)

kcg

3 days ago

[Share On Twitter](https://x.com/intent/post?text=&url=https%3A%2F%2Fwww.cnx-software.com%2F2026%2F10%2F19%2Faxera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost%2F%23comment-662760 "Share On Twitter")

Probably overpriced for the delivered performance, but since this is so far on the paper only, let’s wait and see.

Reply

![Alex](https://gravatar.webp.se/avatar/d903aef5ca2d405fd6c9b1ac464691a1ac8c1444adfcee97ecde12c49317139f?s=128&d=mm&r=g)

Alex

1 day ago

[Share On Twitter](https://x.com/intent/post?text=&url=https%3A%2F%2Fwww.cnx-software.com%2F2026%2F10%2F19%2Faxera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost%2F%23comment-662881 "Share On Twitter")

So, China is now leading in AI models architectures, and it’s just a question of time before they will converge models and hardware and will start to sell bundles. They also lured in quite a few world class scientists on math, fundamental physics, material science, biotechnology, gene engineering. My estimation is that a well-designed LLM trained on properly cleaned up data should be in single digit Tb range size, with most of the slices streamed on demand to memory, so say 128Gb working set plus 128Gb for experts. Under “well designed” I mean something closer to the real brain, “converging”… Read more »

Reply

[![Boardcon Amlogic A311Y3 system-on-module with 8 TOPS AI performance](https://www.cnx-software.com/wp-content/uploads/2026/09/Amlogic-A311Y3-system-on-module.webp)](https://url5.cnx-software.com/tfQkv)

wpDiscuz

Insert

Copy link

✓

Thanks for sharing!

Find any service

[AddToAny](https://www.addtoany.com/ "Share Buttons")

[More…](https://www.cnx-software.com/2026/10/19/axera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost/#addtoany "Show all")

A2A