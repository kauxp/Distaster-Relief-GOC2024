const disasterImageHolder = document.getElementById("imageViewer");
const fileSelector = document.getElementById("fileUploader");


async function uploadDisasterImage() {
    const file = fileSelector.files[0];
    const formData = new FormData();
    formData.append("file", file);
    const response = await fetch("http://localhost:8000/predict", {
        method: "POST",
        body: formData,
    });
    const data = await response.json();
    console.log(data);
    alert("The area is affected by a "+ data['disaster']+ ". Raising alert for the same.");
}


fileSelector.addEventListener("change", (event) => {
    const file = event.target.files[0];
    const imageUrl = URL.createObjectURL(file);
    disasterImageHolder.style.backgroundImage = "url('" + imageUrl + "')";
    uploadDisasterImage();
});

