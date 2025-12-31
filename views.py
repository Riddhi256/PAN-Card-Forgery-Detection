import cv2
import numpy as np
import os
from django.shortcuts import render
from django.conf import settings
from skimage.metrics import structural_similarity as ssim

# Exact reference image path based on your structure
REFERENCE_IMAGE_PATH = settings.MEDIA_ROOT / "reference\original.png"


def upload_image(request):
    if request.method == "POST":

        # Safety check: reference image must exist
        if not os.path.exists(REFERENCE_IMAGE_PATH):
            raise FileNotFoundError(
                f"Reference PAN image not found at {REFERENCE_IMAGE_PATH}"
            )

        # Get uploaded image
        uploaded_file = request.FILES.get("uploaded_pan")
        if not uploaded_file:
            return render(request, "detector/upload.html", {
                "error": "No image uploaded"
            })

        # Load reference image
        reference = cv2.imread(str(REFERENCE_IMAGE_PATH))
        if reference is None:
            raise ValueError("Failed to load reference image")

        # Decode uploaded image
        uploaded_np = cv2.imdecode(
            np.frombuffer(uploaded_file.read(), np.uint8),
            cv2.IMREAD_UNCHANGED
        )

        if uploaded_np is None:
            return render(request, "detector/upload.html", {
                "error": "Invalid uploaded image"
            })

        # Handle RGBA uploads safely
        if len(uploaded_np.shape) == 3 and uploaded_np.shape[2] == 4:
            uploaded_np = cv2.cvtColor(uploaded_np, cv2.COLOR_BGRA2BGR)

        # Resize uploaded image to match reference
        uploaded_np = cv2.resize(uploaded_np, (reference.shape[1], reference.shape[0]))

        # Convert to grayscale
        ref_gray = cv2.cvtColor(reference, cv2.COLOR_BGR2GRAY)
        upl_gray = cv2.cvtColor(uploaded_np, cv2.COLOR_BGR2GRAY)

        # Compute SSIM
        score, _ = ssim(ref_gray, upl_gray, full=True)

        return render(request, "detector/upload.html", {
            "score": round(score * 100, 2)
        })

    return render(request, "detector/upload.html")
