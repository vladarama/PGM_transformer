# PGM_transformer

live demo: TODO

This web application makes various conversions on user uploaded PGM images and returns those converted images back to the user. PGM (Portable Grey Map) files store grayscale 2D images in a specific format that makes it very interesting to work with. 

The foundation of this project was part of a class assignment, where we had to create processing.py, a python script that loads, converts and saves various PGM images. The conversion process includes many transformations that can be applied to PGM images such as:
* Compression
* Decompression
* Color Inversion (Black to White and vice versa)
* Horizontal Flipping
* Vertical Flipping
* Cropping

I decided to take this project away from the classroom, by building a web application using Flask and hosting it on a cloud platform like Heroku. The goal of my application was to allow users to upload their own PGM images, apply a transformation on them and download their transformed image. This project was quite a challenge, because I was forced to learn Flask, a framework I never used before. 
