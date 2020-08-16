// function headerHover(x) {
//     // Light navy: #286086
//     x.style.backgroundColor = "#B0E0E6";
// }
// function headerUnhover(x) {
//     // Mich Blue: #00274C
//     x.style.backgroundColor = "#87CEFA"
// }

// function change_pics() {
//     const image_urls = await fetchImgNames();
//     console.log(image_urls);
//     console.log('done.');
// }

function getImagePath(){
    fetch('/api/randomurl/', {credentials: "same-origin"})
    .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
    })
    .then((data) => {
        console.log(data['img_url'])
        document.getElementById('photo_change').src=data['img_url'];
    })
    .catch((error) => console.log(error));
}