function changeImage(element) {

    var main_prodcut_image = document.getElementById('main_product_image');
    main_prodcut_image.src = element.src;
    

}


let canvas = new fabric.Canvas('tshirt-canvas');

    function updateTshirtImage(imageURL) {
      // If the user doesn't pick an option of the select, clear the canvas
      if (!imageURL) {
        canvas.clear();
      }

      // Create a new image that can be used in Fabric with the URL
      fabric.Image.fromURL(imageURL, function (img) {
        // Define the image as background image of the Canvas
        canvas.setHeight(180);
        canvas.setWidth(150);
        canvas.set({ top: 150, right: 1000 });
        canvas.setBackgroundImage(img, canvas.renderAll.bind(canvas), {
          // Scale the image to the canvas size

          scaleX: canvas.width / img.width,
          scaleY: canvas.height / img.height
        });
      });
    }

    // Update the TShirt color according to the selected color by the user

    // Update the TShirt color according to the selected color by the user
    document.getElementById("tshirt-design").addEventListener("change", function () {

      // Call the updateTshirtImage method providing as first argument the URL
      // of the image provided by the select
      updateTshirtImage(this.value);
    }, false);

    let listElements = document.querySelectorAll('li');

  

    function showImage(imgPath, imgText) {
        var curImage = document.getElementById('main_product_image');
        
        curImage.src = imgPath;
        curImage.alt = imgText;
        curImage.title = imgText;
     }
    