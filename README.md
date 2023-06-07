# <h1>TotalVortex</h1>

Brain computer interface with machine learning based on electoencephalographic data. <br />

<h2>Physionet <br /></h2>
https://physionet.org/content/eegmmidb/1.0.0/ <br />

<h2>Abstract <br /></h2>
This data set consists of over 1500 one- and two-minute EEG recordings, obtained from 109 volunteers, as described below. <br />

<h2>Experimental Protocol <br /></h2>
Subjects performed different motor/imagery tasks while 64-channel EEG were recorded using the BCI2000 system (http://www.bci2000.org). Each subject performed 14 experimental runs: two one-minute baseline runs (one with eyes open, one with eyes closed), and three two-minute runs of each of the four following tasks:<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A target appears on either the left or the right side of the screen. The subject opens and closes the corresponding fist until the target disappears. Then the subject relaxes.<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A target appears on either the left or the right side of the screen. The subject imagines opening and closing the corresponding fist until the target disappears. Then the subject relaxes.<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A target appears on either the top or the bottom of the screen. The subject opens and closes either both fists (if the target is on top) or both feet (if the target is on the bottom) until the target disappears. Then the subject relaxes.<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A target appears on either the top or the bottom of the screen. The subject imagines opening and closing either both fists (if the target is on top) or both feet (if the target is on the bottom) until the target disappears. Then the subject relaxes.<br />

<h2>How to use the program <br /></h2>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Choose the path you want to store the data download in data.py. Then launch it with python3 main.py. Have fun. For predict you can only predict what have been train (patient and experience).

![Screenshot from 2023-06-02 14-39-10](https://github.com/antton-t/TotalVortex/assets/64638111/56ab3e84-62b6-420b-9570-f42254437fe8)
<h2>Event no filter<br /></h2>

![Screenshot from 2023-06-02 14-39-43](https://github.com/antton-t/TotalVortex/assets/64638111/ffbd25d5-756c-4087-9cf6-606b83654b4d)

![Screenshot from 2023-06-02 14-40-02](https://github.com/antton-t/TotalVortex/assets/64638111/bd2bf668-e509-43a2-a845-6165488cc985)

<h2>Event filtered<br /></h2>

![Screenshot from 2023-06-02 14-40-20](https://github.com/antton-t/TotalVortex/assets/64638111/f069f8b0-5064-4138-bfa2-e24368ab0fa8)

<h2>ICA <br /></h2>

![Screenshot from 2023-06-02 14-40-38](https://github.com/antton-t/TotalVortex/assets/64638111/aed5f9c2-41ab-463d-b86e-a3eae412a3ae)
![Screenshot from 2023-06-02 14-41-01](https://github.com/antton-t/TotalVortex/assets/64638111/db34b1eb-9611-4a15-8658-1d836a4605ce)

<h2>Prediction<br /></h2>

![Screenshot from 2023-06-02 14-43-21](https://github.com/antton-t/TotalVortex/assets/64638111/a67bff63-3e1e-4bfc-8d2d-f2adaf8a4f5f)

Acknowledgments <br />
This data set was created and contributed to PhysioBank by Gerwin Schalk (schalk at wadsworth dot org) and his colleagues at the BCI R&D Program, Wadsworth Center, New York State Department of Health, Albany, NY. W.A. Sarnacki collected the data. Aditya Joshi compiled the dataset and prepared the documentation. D.J. McFarland and J.R. Wolpaw were responsible for experimental design and project oversight, respectively. This work was supported by grants from NIH/NIBIB ((EB006356 (GS) and EB00856 (JRW and GS)).
