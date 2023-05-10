let canvas = new fabric.Canvas('tshirt-canvas');
    delBtn = document.getElementById('delete')
    delBtn.style.display = 'none'
    function updateTshirtImage(imageURL){
        fabric.Image.fromURL(imageURL, function(img) {                   
            img.scaleToHeight(300);
            img.scaleToWidth(300); 
            canvas.centerObject(img);
            canvas.add(img);
            canvas.renderAll();
        });
    }
    
    // Update the TShirt color according to the selected color by the user
    document.getElementById("tshirt-color").addEventListener("change", function(){
        document.getElementById("tshirt-div").style.backgroundColor = this.value;
    }, false);

    // Update the TShirt color according to the selected color by the user
    document.getElementById("tshirt-design").addEventListener("change", function(){

        // Call the updateTshirtImage method providing as first argument the URL
        // of the image provided by the select
        updateTshirtImage(this.value);
    }, false);

    // When the user clicks on upload a custom picture
    document.getElementById('tshirt-custompicture').addEventListener("change", function(e){
        var reader = new FileReader();
        
        reader.onload = function (event){
            var imgObj = new Image();
            imgObj.src = event.target.result;

            // When the picture loads, create the image in Fabric.js
            imgObj.onload = function () {
                var img = new fabric.Image(imgObj);

                img.scaleToHeight(120);
                img.scaleToWidth(120); 
                canvas.centerObject(img);
                canvas.add(img);
                canvas.renderAll();
            };
        };

        // If the user selected a picture, load it
        if(e.target.files[0]){
            reader.readAsDataURL(e.target.files[0]);
        }
    }, false);







    $('#addTextButton').on('click', function() {
            var inText = $('#inputText').val();
            
            if(inText.trim() === '') {
              alert('Please type text');
              return;
            }
            
            var inFont = $('#inputFont').val();
            var inSize = 14;
            var inColor = $('#inputColor').val();
            
            var newText = new fabric.Text(inText, {
              fontSize: inSize,
              fontFamily: inFont,
              fill: inColor
            });
            
            newText.on('selected', function() {
              var obJ = canvas.getActiveObject();
              
              // Update Edit Text
              $('#editText').val( obJ.text );
              $('#uiEditFont').dropdown( 'set selected', obJ.fontFamily );
              $('#uiEditFont').dropdown( 'set value', obJ.fontFamily );
              $('#uiEditColor').dropdown( 'set selected', obJ.fill );
              $('#uiEditColor').dropdown( 'set value', obJ.fill );
              
              $('#boxEdit, #boxEditImage').hide();
              $('#boxEditText').show();
            });
            
            canvas.setActiveObject(newText).add(newText);
            
            item_list.push(newText);
          });

    // When the user selects a picture that has been added and press the DEL key
    // The object will be removed !
    document.addEventListener("keydown", function(e) {
        var keyCode = e.keyCode;

        if(keyCode == 46){
            console.log("Removing selected element on Fabric.js on DELETE key !");
            canvas.remove(canvas.getActiveObject());
        }
    }, false);

/* Define as node the T-Shirt Div
var node = document.getElementById('tshirt-div');

domtoimage.toPng(node).then(function (dataUrl) {
// Print the data URL of the picture in the Console
console.log(dataUrl);

// You can for example to test, add the image at the end of the document
var img = new Image();
img.src = dataUrl;
document.body.appendChild(img);
}).catch(function (error) {
console.error('oops, something went wrong!', error);
});

*/

// When a selection is being made
canvas.on({
  'selection:created': () => {
    delBtn.style.display = 'inline-block'
  }
})

// When a selection is cleared
canvas.on({
  'selection:cleared': () => {
    delBtn.style.display = 'none'
  }
})

// Rmove the active object on clicking the delete button
delBtn.addEventListener('click', e => {
  canvas.remove(canvas.getActiveObject())
})





function showImage(imgPath, imgText) {
    var curImage = document.getElementById('currentImg');
    
    curImage.src = imgPath;
    curImage.alt = imgText;
    curImage.title = imgText;
 }


 let canvas1 = new fabric.Canvas('tshirt-canvas1');
 delBtn1 = document.getElementById('delete1')
 delBtn1.style.display = 'none'
 function updateTshirtImage1(imageURL){
     fabric.Image.fromURL(imageURL, function(img) {                   
         img.scaleToHeight(300);
         img.scaleToWidth(300); 
         canvas1.centerObject(img);
         canvas1.add(img);
         canvas1.renderAll();
     });
 }
 
 // Update the TShirt color according to the selected color by the user
 document.getElementById("tshirt-color1").addEventListener("change", function(){
     document.getElementById("tshirt-div1").style.backgroundColor = this.value;
 }, false);

 // Update the TShirt color according to the selected color by the user
 document.getElementById("tshirt-design1").addEventListener("change", function(){

     // Call the updateTshirtImage method providing as first argument the URL
     // of the image provided by the select
     updateTshirtImage1(this.value);
 }, false);

 // When the user clicks on upload a custom picture
 document.getElementById('tshirt-custompicture1').addEventListener("change", function(e){
     var reader = new FileReader();
     
     reader.onload = function (event){
         var imgObj = new Image();
         imgObj.src = event.target.result;

         // When the picture loads, create the image in Fabric.js
         imgObj.onload = function () {
             var img = new fabric.Image(imgObj);

             img.scaleToHeight(120);
             img.scaleToWidth(120); 
             canvas1.centerObject(img);
             canvas1.add(img);
             canvas1.renderAll();
         };
     };

     // If the user selected a picture, load it
     if(e.target.files[0]){
         reader.readAsDataURL(e.target.files[0]);
     }
 }, false);







 $('#addTextButton1').on('click', function() {
         var inText1 = $('#inputText1').val();
         
         if(inText1.trim() === '') {
           alert('Please type text');
           return;
         }
         
         var inFont1 = $('#inputFont1').val();
         var inSize1 = 14;
         var inColor1 = $('#inputColor1').val();
         
         var newText1 = new fabric.Text(inText1, {
           fontSize: inSize1,
           fontFamily: inFont1,
           fill: inColor1
         });
         
         newText1.on('selected', function() {
           var obJ1 = canvas1.getActiveObject();
           
           // Update Edit Text
           $('#editText1').val( obJ1.text );
           $('#uiEditFont1').dropdown( 'set selected', obJ1.fontFamily );
           $('#uiEditFont1').dropdown( 'set value', obJ1.fontFamily );
           $('#uiEditColo1').dropdown( 'set selected', obJ1.fill );
           $('#uiEditColor1').dropdown( 'set value', obJ1.fill );
           
           $('#boxEdit1, #boxEditImage1').hide();
           $('#boxEditText1').show();
         });
         
         canvas1.setActiveObject(newText1).add(newText1);
         
         item_list.push(newText1);
       });

 // When the user selects a picture that has been added and press the DEL key
 // The object will be removed !
 document.addEventListener("keydown", function(e) {
     var keyCode = e.keyCode;

     if(keyCode == 46){
         console.log("Removing selected element on Fabric.js on DELETE key !");
         canvas.remove(canvas.getActiveObject());
     }
 }, false);

/* Define as node the T-Shirt Div
var node = document.getElementById('tshirt-div1');

domtoimage.toPng(node).then(function (dataUrl) {
// Print the data URL of the picture in the Console
console.log(dataUrl);

// You can for example to test, add the image at the end of the document
var img = new Image();
img.src = dataUrl;
document.body.appendChild(img);
}).catch(function (error) {
console.error('oops, something went wrong!', error);
});
*/


// When a selection is being made
canvas1.on({
'selection:created': () => {
 delBtn1.style.display = 'inline-block'
}
})

// When a selection is cleared
canvas1.on({
'selection:cleared': () => {
 delBtn1.style.display = 'none'
}
})

// Rmove the active object on clicking the delete button
delBtn1.addEventListener('click', e => {
canvas1.remove(canvas1.getActiveObject())
})




function showImage1(imgPath, imgText) {
    var curImage = document.getElementById('currentImg1');
    
    curImage.src = imgPath;
    curImage.alt = imgText;
    curImage.title = imgText;
 }




 
 let canvas2 = new fabric.Canvas('tshirt-canvas2');
 delBtn2 = document.getElementById('delete2')
 delBtn2.style.display = 'none'
 function updateTshirtImage2(imageURL){
     fabric.Image.fromURL(imageURL, function(img) {                   
         img.scaleToHeight(300);
         img.scaleToWidth(300); 
         canvas2.centerObject(img);
         canvas2.add(img);
         canvas2.renderAll();
     });
 }
 
 // Update the TShirt color according to the selected color by the user
 document.getElementById("tshirt-color2").addEventListener("change", function(){
     document.getElementById("tshirt-div2").style.backgroundColor = this.value;
 }, false);

 // Update the TShirt color according to the selected color by the user
 document.getElementById("tshirt-design2").addEventListener("change", function(){

     // Call the updateTshirtImage method providing as first argument the URL
     // of the image provided by the select
     updateTshirtImage2(this.value);
 }, false);

 // When the user clicks on upload a custom picture
 document.getElementById('tshirt-custompicture2').addEventListener("change", function(e){
     var reader = new FileReader();
     
     reader.onload = function (event){
         var imgObj = new Image();
         imgObj.src = event.target.result;

         // When the picture loads, create the image in Fabric.js
         imgObj.onload = function () {
             var img = new fabric.Image(imgObj);

             img.scaleToHeight(50);
             img.scaleToWidth(50); 
             canvas2.centerObject(img);
             canvas2.add(img);
             canvas2.renderAll();
         };
     };

     // If the user selected a picture, load it
     if(e.target.files[0]){
         reader.readAsDataURL(e.target.files[0]);
     }
 }, false);







 $('#addTextButton2').on('click', function() {
         var inText2 = $('#inputText2').val();
         
         if(inText2.trim() === '') {
           alert('Please type text');
           return;
         }
         
         var inFont2 = $('#inputFont2').val();
         var inSize2 = 14;
         var inColor2 = $('#inputColor2').val();
         
         var newText2 = new fabric.Text(inText2, {
           fontSize: inSize2,
           fontFamily: inFont2,
           fill: inColor2
         });
         
         newText2.on('selected', function() {
           var obJ2 = canvas2.getActiveObject();
           
           // Update Edit Text
           $('#editText2').val( obJ2.text );
           $('#uiEditFont2').dropdown( 'set selected', obJ2.fontFamily );
           $('#uiEditFont2').dropdown( 'set value', obJ2.fontFamily );
           $('#uiEditColo2').dropdown( 'set selected', obJ2.fill );
           $('#uiEditColor2').dropdown( 'set value', obJ2.fill );
           
           $('#boxEdit2, #boxEditImage2').hide();
           $('#boxEditText2').show();
         });
         
         canvas2.setActiveObject(newText2).add(newText2);
         
         item_list.push(newText2);
       });

 // When the user selects a picture that has been added and press the DEL key
 // The object will be removed !
 document.addEventListener("keydown", function(e) {
     var keyCode = e.keyCode;

     if(keyCode == 46){
         console.log("Removing selected element on Fabric.js on DELETE key !");
         canvas.remove(canvas.getActiveObject());
     }
 }, false);

/* Define as node the T-Shirt Div
var node = document.getElementById('tshirt-div2');

domtoimage.toPng(node).then(function (dataUrl) {
// Print the data URL of the picture in the Console
console.log(dataUrl);

// You can for example to test, add the image at the end of the document
var img = new Image();
img.src = dataUrl;
document.body.appendChild(img);
}).catch(function (error) {
console.error('oops, something went wrong!', error);
});
*/


// When a selection is being made
canvas2.on({
'selection:created': () => {
 delBtn2.style.display = 'inline-block'
}
})

// When a selection is cleared
canvas2.on({
'selection:cleared': () => {
 delBtn2.style.display = 'none'
}
})

// Rmove the active object on clicking the delete button
delBtn2.addEventListener('click', e => {
canvas2.remove(canvas2.getActiveObject())
})



function showImage2(imgPath, imgText) {
    var curImage = document.getElementById('currentImg2');
    
    curImage.src = imgPath;
    curImage.alt = imgText;
    curImage.title = imgText;
 }