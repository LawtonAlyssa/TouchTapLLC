window.addEventListener('load', loadEvent)

function loadEvent() {
    console.log("html loaded!")
    $(document).ready(function () {
        if (window.File && window.FileList && window.FileReader) {
            $("#files").on("change", function (e) {
                var files = e.target.files,
                    filesLength = files.length;
                for (var i = 0; i < filesLength; i++) {
                    var f = files[i]
                    // console.log(f)

                    if (f.type === "application/pdf") {
                        console.log("PDF!")
                    } else {
                        var fileReader = new FileReader();
                        fileReader.onload = (function (e) {
                            var file = e.target;

                            //previous
                            // $("<span class=\"pip\">" +
                            //     "<img class=\"imageThumb\" src=\"" + e.target.result + "\" title=\"" + file.name + "\"/>" +
                            //     "<br/><span class=\"remove\">Remove image</span>" +
                            //     "</span>").insertAfter("#files");

                            // modified v-1
                            // $("<div class=\"card\">" +
                            //     "<img class=\"card-img\" src=\"" + e.target.result + "\" title=\"" + file.name + "\"/>" +
                            //     "<br/><div class=\"card-img-overlay text-right\">"+
                            //     "<br/><button type=\"button\" class=\"btn btn-danger\"><i class=\"fa fa-trash fa-lg\"></i></button>"+
                            //     "<br/></div>" +
                            //     "<br/></div>").insertAfter("#files");

                            // modified v-2
                            document.getElementById("photo-preview").innerHTML += "<div class=\"col mb-4\"> "+
                            "<br/><div class=\"card\">" +
                            "<br/><img class=\"card-img\" src=\"" + e.target.result + "\" alt=\"" + file.name + "\"/>" +
                            "<br/><div class=\"card-img-overlay text-right\">"+
                            "<br/><a class=\"close\" href=\"#\"><i class=\"fa fa-trash fa-lg\"></i></a>"+
                            "<br/></div>" +
                            "<br/></div>" +
                            "<br/></div>";

                            // Old code here
                            /*$("<img></img>", {
                              class: "imageThumb",
                              src: e.target.result,
                              title: file.name + " | Click to remove"
                            }).insertAfter("#files").click(function(){$(this).remove();});*/

                        });
                        fileReader.readAsDataURL(f);
                    }

                }
            });
        } else {
            alert("Your browser doesn't support to File API")
        }
    });

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