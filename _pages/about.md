---
permalink: /
title: "Junkai Tan / 谭浚楷"
layout: single
excerpt: "Junkai Tan is a second-year graduate student from School of Electrical Engineering, Xi'an Jiaotong University. His research interest include robotics control, intelligent control, learning-based control, and unmanned system control."
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---


<!-- ## 👨‍💼 About Me | 个人简介 -->
I’m a second-year graduate student from [School of Electrical Engineering](https://ee.xjtu.edu.cn/), [Xi'an Jiaotong University](https://www.xjtu.edu.cn/). My research interest include *robotics control*, *intelligent control*, *learning-based control*, and *unmanned system control*.
<!-- - 🌐 Personal Website: [tanjunkai2001.github.io](https://tanjunkai2001.github.io) -->

I am very fortunate to be advised by [Prof. Hui Cao](http://gr.xjtu.edu.cn/en/web/huicao) and [Prof. Shuangsi Xue](https://gr.xjtu.edu.cn/en/web/xssxjtu) of BIR Lab, Xi'an Jiaotong University. I am also a student of the [Industrial Automation Lab](https://ee.xjtu.edu.cn/szdw/bssds/gyzdhjys.htm).

## 🔬 Research Interests
My research interests focus on two primary areas:

- **Data-Driven Unmanned Systems Approximate Optimal Control**  
  Developing control algorithms that leverage data to optimize unmanned system performance  
  *Published in **IEEE TASE**, **INS**, **Nonlinear Dynamics***

- **Human-Machine Hybrid Enhanced Shared Optimal Control**  
  Creating systems that combine human expertise with machine capabilities for superior control  
  *Published in **Neurocomputing**, **IJRNC**, **JAI***

<!-- ## 💻 Core Competencies
- **Theoretical Research**: Solid foundation in advanced control and reinforcement learning theory. Leading research on human-machine hybrid control with publications in top journals including IEEE TASE, Information Sciences, and Nonlinear Dynamics.
- **Engineering Practice**: Extensive experience with unmanned systems development, including UAV-UGV collaborative control projects and multi-unmanned system hardware platforms based on optical motion capture systems. -->

## 📝 Selected Publications

<!-- 1. "[Prescribed performance robust approximate optimal tracking control via Stackelberg game](https://ieeexplore.ieee.org/document/10916718)", *IEEE Transactions on Automation Science and Engineering*, 2025.
2. "[Finite-time safe reinforcement learning control of multi-player nonzero-sum game for quadcopter systems](https://www.sciencedirect.com/science/article/pii/S002002552500249X)", *Information Sciences*, 2025.
3. "[Unmanned aerial-ground vehicle finite-time docking control via pursuit-evasion games](https://link.springer.com/10.1007/s11071-025-11021-6)", *Nonlinear Dynamics*, 2025.
4. "[Data-driven optimal shared control of unmanned aerial vehicles](https://www.sciencedirect.com/science/article/pii/S0925231225001006)", *Neurocomputing*, 2025. -->


{% for post in site.publications reversed %}
  {% if post.pubtype == 'journal' %}
    {% include archive-single-home_V2.html %}
  {% endif %}
{% endfor %}


Detailed publications and open-source code can be found in my [Publications](https://tanjunkai2001.github.io/publications/) page.

## 📄 Curriculum Vitae
You can find my CV here: [Web Version](https://tanjunkai2001.github.io/cv/) | [English PDF](../assets/Curriculum_Vitae.pdf) | [Chinese PDF](../assets/简历_谭浚楷_中文_V2.pdf)

## 🔗 Connect With Me
[![Google Scholar](https://img.shields.io/badge/Google_Scholar-4285F4?style=for-the-badge&logo=google-scholar&logoColor=white)](https://scholar.google.com/citations?user=KrOQdKAAAAAJ&hl=zh-CN) [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/tanjunkai2001) [![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:tanjk@stu.xjtu.edu.cn) [![WeChat](https://img.shields.io/badge/WeChat-07C160?style=for-the-badge&logo=wechat&logoColor=white)](../images/Wechat.jpg) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/junkai-tan-366790268/)


<!-- ## 📫 Contact | 联系方式
- 📧 Email: tanjk@stu.xjtu.edu.cn -->


<div style="display: flex; align-items: center; justify-content: space-between;">
  <img src="https://github-readme-stats-weld-six-22.vercel.app/api/top-langs/?username=tanjunkai2001&layout=compact" alt="Top Languages" height="150" />
  <img src="https://github-readme-stats-weld-six-22.vercel.app/api?username=tanjunkai2001&count_private=true&show_icons=true" alt="GitHub Stats" height="150" />
</div>




<!-- # 我的位置

这是我在香港大学的地址，显示在地图上： -->

<div id="map" style="height: 400px; width: 100%;"></div>

<script>
  var map = L.map('map').setView([22.2855, 114.1585], 13);  // 设置位置坐标（香港大学）
  
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);
  
  L.marker([22.2855, 114.1585]).addTo(map)
    .bindPopup('Rm 801 Chow Yei Ching Building, The University of Hong Kong')
    .openPopup();
</script>

<head>
  <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
  <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
</head>