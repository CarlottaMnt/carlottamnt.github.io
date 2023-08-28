---
title: 
layout: single
classes: wide
permalink: /teaching/
---
<br/> 

<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-PNS829G"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

# <center> Teaching and Tutorials </center>
- - -
**Regression Discontinuity Designs: theory and simulations**. Exeter Reading Group (EMERG), May 2023  <br/>
<small>[ <a href="#/" onclick="visib('abstractRDD')">Overview</a> | [Slides][slides]]</small>

<div id="abstractRDD" style="display: none; text-align: justify; line-height: 1.2" ><small>
I present Sharp Regression Discontinuity Design (RDD) and Fuzzy Design (FRD) for causal inference. I analyze how Ordinary Least Squares (OLS) and Local Linear Polynomial estimators perform when data-generating processes deviate from assumptions. Through simulations, I uncover the consistency and limitations of these estimators in non-ideal scenarios. This lecture fosters a cautious approach to interpretation, highlighting the need to assess estimator behaviour in the presence of assumption mismatches.
</small><br><br/></div>

[slides]:{{ site.baseurl }}{% link assets/files/EMERG_RDD.pdf %}

**An introduction to UL HPC supercomputers: performances, functionalities and accessibility**. Centre of Competence for Data Science and Simulation, February 2023 <br/>
<small>[ <a href="#/" onclick="visib('abstract')">Overview</a> | [Slides][slides]]</small>

<div id="abstract" style="display: none; text-align: justify; line-height: 1.2" ><small>
High-performance computers, also known as supercomputers, are specialized machines that perform highly advanced and complex computing tasks. They can solve problems that are too large or complex for regular computers. 
Since 2007, the University of Luxembourg (UL) has been operating a sizeable academic HPC facility that remains one of the references for HPC implementations within the country, offering a cutting-edge research infrastructure to Luxembourg public research. 
In this lunch session, I illustrate the HPC computational abilities. I discuss some UL HPC functionalities. Finally, I present some technical requirements for accessing and using this tool.
</small><br><br/></div>

[slides]:{{ site.baseurl }}{% link assets/files/HPC_Talk_CompetenceCenter.pdf %}

**Introduction to Machine learning methods. LISER training course, Januray 2023** <br/>
<small>[ <a href="#/" onclick="visib('tutorial')">Tutorials</a> | [Overview][overview]]</small>

<div id="tutorial" style="display: none; text-align: justify; line-height: 1.2">
  <ul>
    <li><a href="https://colab.research.google.com/drive/1DfI05FBO829VrpxRneV3d2pc9ZeIKrcn?usp=sharing">Predictor set</a></li>
    <li><a href="https://colab.research.google.com/drive/1A-6kw0lHkIZKnDqQmch3fcRT4r3QJrPR?usp=sharing">Cross-Validation</a></li>
    <li><a href="https://colab.research.google.com/drive/10Gdn7eGRXLO04OtVRuDilYtgsUIMk5nx?usp=sharing">Loss functions</a></li>
    <li><a href="https://colab.research.google.com/drive/1vMfSsVjJBZb8D4JX3LpZRUDASfvLlvVL?usp=sharing">Classification models</a></li>
    <li><a href="https://colab.research.google.com/drive/1-42OuE4HbOiYa7PGouRpBGBVncQJSos4?usp=sharing">Neural Networks</a></li>
    <li><a href="https://colab.research.google.com/drive/18gQTRbAe_LRP5Wnd_ka7HgYKsVZ9IBjh?usp=sharing">Convolutional Neural Networks for image classification</a></li>
  </ul>
</div>

[overview]:{{ site.baseurl }}{% link assets/files/Overview-day-2.pdf %}
<script>
function visib(id) {
  var x = document.getElementById(id);
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script>


