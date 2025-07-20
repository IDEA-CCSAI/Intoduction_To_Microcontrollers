# <h1>**Intoduction_To_Microcontrollers**</h1>

### Sections:
- [Event Information](#event-information)  
- [Update Information (Important if attended last event)](#important-info)  
- [Files Included in Repo](#files-included-in-repo)  
- [Setup of IDE, and Installations](#setup)  
- [ESP Pinout and Important Features](#esp-pinout-and-important-features)  
- [Resources to Get Your Own Kit](#resources)  
- [Key Takeaways](#key-takeaway)  


---

## <h2>**_Event Information_**</h2>

This repository is on the event of **Introduction to MicroControllers**.  
It contains a fast lecture on microcontrollers, embedded devices, and IoT devices.  
In addition, there is also a workshop segment to build your own motion sensor, send a signal to a simple frontend (HTML, CSS, and JavaScript), and send a notification to a user’s mobile device via the [Pushover mobile app](https://pushover.net/).

---

## <h2>**_Important Info_**</h2>

- If you attended the last event, many participants faced issues with the ESP32 not connecting to Wi-Fi reliably. After further research, we found a configuration that stabilizes radio signals and reduces antenna reflections when connecting to Wi-Fi.  

  The code is:  
  `[wlan.config(txpower=8.5)]`  
  It is already included in this repo’s code.  
  Credit to [the_merc](https://forum.arduino.cc/t/no-wifi-connect-with-esp32-c3-super-mini/1324046/13) for the solution.

- During the lecture, we used a private MQTT broker.  
  Since this repository is public, the broker IP has been removed. If you still have the broker IP from the event, you can keep using it—it’s still functional **for now**, but there is no guarantee it will always remain available. It may work for a few months, but don’t rely on it long term.  

  Please:
  - Avoid sending any private data through this broker.
  - Use a very unique topic to avoid interference with other users.

- If you plan to use 3D pinting for this project, or any other personal projects. Centennial College library offers free 3d printing for each students up to 100 grams. For this project, the case is 21.59 grams.

---

## <h2>**_Files Included in Repo_**</h2>

This repository contains:
- Code and diagrams related to the ESP32.  
- The presentation slides.  
- Pushover setup instructions.  
- Additional scripts for testing on your computer.

---

## <h2>**_Setup_**</h2>

1. Install the drivers for your computer to recognize ESP devices:  
   [Silicon Labs VCP Drivers](https://www.silabs.com/software-and-tools/usb-to-uart-bridge-vcp-drivers)  
   - Head to **Downloads**.  
   - Choose **CP210x VCP Windows** (3rd option).  
   - Unzip and run the `.exe` matching your system architecture.

2. Download **MicroPython**:  
   [micropython.org](https://micropython.org/)  
   - This event used the [ESP32-C3 Mini](https://micropython.org/download/LOLIN_C3_MINI/).  
   - If you are using a different microcontroller, find it on the download page.

3. Install **Thonny IDE**:  
   [Thonny](https://thonny.org/)


If you want a video version of this steps cheack out [TechToTiknker on how to get started in micropython](https://www.youtube.com/watch?v=elBtWZ_fOZU&list=PLw0SimokefZ3uWQoRsyf-gKNSs4Td-0k6)

---

## <h2>**_ESP Pinout and Important Features_**</h2>

<img width="960" height="567" alt="image" src="https://github.com/user-attachments/assets/ca812ece-9ded-41d4-9784-26d440f2fbcb" />

If your ESP32 has not been flashed with firmware, or it’s stuck in a loop and won’t allow code uploads:  
1. Hold the **BOOT** button.  
2. Press the **RESET** button.  
3. Release **RESET**, then release **BOOT**.  

This puts the ESP32 into **flash mode**, ready to accept new code.

---

## <h2>**_Resources_**</h2>

Below are some links for electronic kits compatible with the ESP32.  

If you prefer alternatives, AliExpress often has good prices, but ensure products have solid reviews before purchasing. Amazon kits tend to be more expensive but usually offer more components in their kits and reliable customer service. Arduino and Raspberry Pi kits are also compatible with the ESP32. While AliExpress does have customer service, it is generally less reliable than Amazon’s.


- [$12](https://www.aliexpress.com/item/1005006065671964.html?spm=a2g0o.productlist.main.9.3f2155483RmJlb&algo_pvid=f38f32e2-8779-4d16-9f36-0a8e71b9871d&algo_exp_id=f38f32e2-8779-4d16-9f36-0a8e71b9871d-18&pdp_ext_f=%7B%22order%22%3A%222251%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21CAD%2181.29%2120.44%21%21%21414.95%21104.32%21%402103247017507289474617626ea454%2112000035571056896%21sea%21CA%210%21ABX&curPageLogUid=TAk9W5iUDe2I&utparam-url=scene%3Asearch%7Cquery_from%3A)
- [$25 Regular Esp32 inlcuded](https://www.aliexpress.com/item/1005007342848559.html?spm=a2g0o.productlist.main.32.3b2373893ahhon&aem_p4p_detail=20250720103117629630497150560003926935&algo_pvid=ade768d8-58f3-4b5e-9e03-e063d335ff90&algo_exp_id=ade768d8-58f3-4b5e-9e03-e063d335ff90-31&pdp_ext_f=%7B%22order%22%3A%222211%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21CAD%21132.70%2143.79%21%21%21678.08%21223.76%21%402101e7f617530326769567072ed2fc%2112000040348428333%21sea%21CA%216245576330%21X&curPageLogUid=g9qlSi5fOInk&utparam-url=scene%3Asearch%7Cquery_from%3A&search_p4p_id=20250720103117629630497150560003926935_9)  
- [$32 Arduino Uno R3 included](https://www.aliexpress.com/item/1005007342848559.html?spm=a2g0o.productlist.main.32.3b2373893ahhon&aem_p4p_detail=20250720103117629630497150560003926935&algo_pvid=ade768d8-58f3-4b5e-9e03-e063d335ff90&algo_exp_id=ade768d8-58f3-4b5e-9e03-e063d335ff90-31&pdp_ext_f=%7B%22order%22%3A%222211%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21CAD%21132.70%2143.79%21%21%21678.08%21223.76%21%402101e7f617530326769567072ed2fc%2112000040348428333%21sea%21CA%216245576330%21X&curPageLogUid=g9qlSi5fOInk&utparam-url=scene%3Asearch%7Cquery_from%3A&search_p4p_id=20250720103117629630497150560003926935_9)  
- [$18 Arduino Uno R3 included](https://www.aliexpress.com/item/1005006477517942.html?spm=a2g0o.productlist.main.3.3b2373893ahhon&algo_pvid=ade768d8-58f3-4b5e-9e03-e063d335ff90&algo_exp_id=ade768d8-58f3-4b5e-9e03-e063d335ff90-2&pdp_ext_f=%7B%22order%22%3A%22320%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21CAD%2132.21%2127.38%21%21%21164.59%21139.91%21%402101e7f617530326769567072ed2fc%2112000037344481958%21sea%21CA%216245576330%21X&curPageLogUid=MGAXxAbMfpDb&utparam-url=scene%3Asearch%7Cquery_from%3A)  

 Please keep in mind that prices can change due to limited-time offers. Additionally, AliExpress often provides discounts for new accounts or during special sales events, so prices may vary depending on these conditions.


---

## <h2>**_Key Takeaway_**</h2>

If you followed along, congratulations!  
This serves as a strong starting point if you plan to explore **hardware projects** or **IoT development**.  

At the end of this file, there are links to YouTube videos showing what can be done with ESP boards—but really, **the sky’s the limit** for your projects.

Expect **more events in the future** covering microcontrollers and IoT. Stay tuned!  

For questions, feel free to join our [Discord](https://discord.gg/vV8pJHYWdX).




**<h3> Projects done by esp's </h3>**

- [Porsche Taillights](https://www.youtube.com/watch?v=VImyvvERbCI) (Says aurdiono but esp)
- [Dasai Mochi](https://www.youtube.com/watch?v=jEvsJSZWH9U)
- [Plant watering system](https://www.youtube.com/watch?v=Ix3a3ThsHfA)
- [Haptic knob](https://www.youtube.com/watch?v=Q76dMggUH1M) (Its way more advance and its own pcb, but the brain is an esp32. Had to include since its an amazing project with a lot of details)

---


