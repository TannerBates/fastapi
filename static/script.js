document.addEventListener("DOMContentLoaded", () => {
    // NASA APOD API endpoint on your FastAPI server
    const apiUrl = "http://127.0.0.1:8000/apod/";

    // Fetch data from the API and display it on the page
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            document.getElementById("title").textContent = data.title;
            document.getElementById("date").textContent = `Date: ${data.date}`;
            document.getElementById("explanation").textContent = data.explanation;

            const apodImage = document.getElementById("apod-image");
            apodImage.src = data.url;
            apodImage.alt = data.title;

            if (data.media_type === "video") {
                // If the media type is a video, replace the image with an iframe
                apodImage.style.display = "none";
                const iframe = document.createElement("iframe");
                iframe.src = data.url;
                iframe.width = "100%";
                iframe.height = "400";
                document.querySelector(".apod-container").appendChild(iframe);
            }
        })
        .catch(error => console.error("Error fetching APOD data:", error));
});