window.onload=function() {
    document.getElementById("upload-button").style.display='none';
}
window.addEventListener('load', loadEvent)

var file_srcs = []

var body = ""

function loadEvent() {
    console.log("html loaded!")

    // if (localStorage.getItem("file_srcs") == null) {
    //     console.log("Created file_srcs")
    //     file_srcs = [];
    //     localStorage.setItem("file_srcs", JSON.stringify(file_srcs));
    // }
    $(document).ready(function() {
        if (window.File && window.FileList && window.FileReader) {
            showUploadButton();

            $("#files").on("change", function(e) {
                var files = e.target.files,
                    filesLength = files.length;

                for (var i = 0; i < filesLength; i++) {
                    var f = files[i]
                    var f_name = f.name

                    console.log("file name: " + f_name)

                    

                    
                    // body+= f;
                    // body += "<img src=" + f_name + " alt=\"Unable to upload file\">"


                    // var file_id = parseInt(localStorage.getItem("file_id")) + 1;

                    // localStorage.setItem("file_id", file_id.toString())

                    if (f.type === "application/pdf") {
                        console.log("PDF!")
                    } else {
                        var fileReader = new FileReader();

                        fileReader.onload = (function(e) {
                            var file = e.target;

                            // const newImage = new Image(100, 200);
                            // newImage.src = file.result;

                            // var canvas = document.createElement("canvas");
                            // context = canvas.getContext('2d');
                            
                            // makeBase(file);

                            // var pngUrl = canvas.toDataURL();

                            // body += pngUrl;

                            // body+=getBase64Image(newImage);

                            // body += "<img src=" + f_name + " alt=\"Unable to upload file\">"

                            // file_srcs = JSON.parse(localStorage.file_srcs);
                            // file_srcs.push(file.result);
                            // localStorage.setItem("file_srcs", JSON.stringify(file_srcs));

                            // console.log("name" + f_name);

                            // previous
                            // $("<span class=\"pip\">" +
                            //     "<img class=\"imageThumb\" src=\"" + e.target.result + "\" title=\"" + f_name + "\"/>" +
                            //     "<br/><span class=\"remove\">Remove image</span>" +
                            //     "</span>").insertAfter("#files");

                             // previous
                            // $("<img src=\"" + e.target.result+ "\"/ >").insertAfter("#files");

                            // modified v-1
                            // $("<div class=\"card\">" +
                            //     "<img class=\"card-img\" src=\"" + e.target.result + "\" title=\"" + file.name + "\"/>" +
                            //     "<br/><div class=\"card-img-overlay text-right\">"+
                            //     "<br/><button type=\"button\" class=\"btn btn-danger\"><i class=\"fa fa-trash fa-lg\"></i></button>"+
                            //     "<br/></div>" +
                            //     "<br/></div>").insertAfter("#files");

                            // modified v-2

                            // document.getElementById("photo-preview").innerHTML += "<div class=\"col mb-4\"> " +
                            //     "<br/><div class=\"card\">" +
                            //     "<br/><img class=\"card-img\" src=\"" + file.result + "\" alt=\"" + f_name + "\"/>" +
                            //     "<br/><div class=\"card-img-overlay text-right\" id=\"file_" + file_id + "\">" +
                            //     "<br/><button class=\"close\" id=\"file_" + file_id + "\" href=\"#\"><i class=\"fa fa-trash fa-lg\"></i></button>" +
                            //     "<br/></div>" +
                            //     "<br/></div>" +
                            //     "<br/></div>";


                            // Old code here
                            $("<img></img>", {
                                class: "card-img mx-2",
                                src: file.result,
                                title: file.name + " | Click to remove"
                            }).insertAfter("#files").click(function() {
                                // file_srcs = JSON.parse(localStorage.file_srcs);
                                // console.log($(this));
                                // file_srcs = removeItemOnce(file_srcs, $(this).src);
                                $(this).remove();
                            });


                        });

                        fileReader.readAsDataURL(f);
                    }

                }
            });
        } else {
            alert("Your browser doesn't support to File API")
        }

        // document.getElementById("upload-button").onclick = function () {
        //     window.open('mailto:alawton1@my.hpu.edu?subject=Touch Tap LLC, Braille Transcription Request&body=' + encodeURIComponent(body));
        // }
    });



    // if (document.querySelector('.close') != null) {
    //     console.log("HERE")
    //     document.querySelector('.close').onclick(function() {
    //         $(this).remove();
    //     });
    // }

}

function htmlToText(html) {
    var temp = document.createElement('div');
    temp.innerHTML = html;
    return temp.textContent;
}

function removeItemOnce(arr, value) {
    var index = arr.indexOf(value);
    if (index > -1) {
        arr.splice(index, 1);
    }
    return arr;
}

function showUploadButton() {
    document.getElementById("upload-button").style.display='block';
}

function getBase64Image(img) {
    // Create an empty canvas element
    var canvas = document.createElement("canvas");
    canvas.width = img.width;
    canvas.height = img.height;

    // Copy the image contents to the canvas
    var ctx = canvas.getContext("2d");
    ctx.drawImage(img, 0, 0);

    // Get the data-URL formatted image
    // Firefox supports PNG and JPEG. You could check img.src to
    // guess the original format, but be aware the using "image/jpg"
    // will re-encode the image.
    var dataURL = canvas.toDataURL("image/png");

    return dataURL.replace(/^data:image\/(png|jpg);base64,/, "");
}

function makeBase(img) {
    baseImage = new Image();
    baseImage.src = img.result;
    baseImage.onload = function() {
        context.drawImage(baseImage, 100, 100);
    }
}

/* PDF Coversion ---
document.querySelector(".embed-link").addEventListener("click", function (e){

    e.preventDefault();

    this.setAttribute("class", "hidden");

    var options = {
        pdfOpenParams: {
            pagemode: "thumbs",
            navpanes: 0,
            toolbar: 0,
            statusbar: 0,
            view: "FitV"
        }
    };

    var myPDF = PDFObject.embed("../pdf/sample-3pp.pdf", "#pdf", options);

    var el = document.querySelector("#results");
    el.setAttribute("class", (myPDF) ? "success" : "fail");
    el.innerHTML = (myPDF) ? "PDFObject successfully added an &lt;embed> element to the page!" : "Uh-oh, the embed didn't work.";

});
*/