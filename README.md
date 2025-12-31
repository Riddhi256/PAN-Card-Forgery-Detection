# PAN Card Forgery Detection Using Structural Similarity

This project implements an image-based PAN card forgery detection system using classical computer vision techniques.

## Overview
The system verifies the authenticity of a PAN card by comparing a reference image with a test image to identify structural inconsistencies that may indicate forgery.

## Methodology
- Structural Similarity Index (SSIM) is used to measure visual similarity between the original and test PAN card images.
- Image preprocessing is performed using OpenCV to ensure consistent comparison.
- Contour detection techniques are applied to localize regions with significant structural mismatch.

## System Implementation
- The application is developed using Django, providing a simple web interface for image upload.
- Backend processing handles image comparison and forgery detection.
- Emphasis is placed on accuracy, robustness, and interpretability of results.

## Technologies Used
- Python
- Django
- OpenCV
- scikit-image (SSIM)
- NumPy
- scikit-learn

## Outcome
The system successfully detects forged regions by highlighting structural differences between PAN card images, demonstrating the effectiveness of SSIM-based image comparison for document verification tasks.
