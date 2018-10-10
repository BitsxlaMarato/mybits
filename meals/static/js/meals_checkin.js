
let meals_webcam = (()=>{
    let obj = {}
    let cams = []

    obj.initScanner = ()=>{
        Instascan.Camera.getCameras().then(function (cameras) {
            if (cameras.length > 0) {
                cams = cameras
                console.log(cams)
            } else {
                console.error('No cameras found.');
            }
        }).catch(function (e) {
            console.error(e);
        });
    }

    obj.initListeners = ()=>{
        $(window).on("load", function(){
	    obj.imageScan()
        })
    }

    //Opens a popup with a camera preview. If a QR is detected,
    //it's value is set into 'inputElem'.
    //Clicking the bg cancels the operation
    //pre: call initScanner
    obj.imageScan = ()=>{
        if(!cams) console.error("I can't scan without a camera")
        if(!localStorage.getItem("selectedCam"))
            localStorage.setItem("selectedCam", 0)

        let selectedCam = parseInt(localStorage.getItem("selectedCam"))
        if (isNaN(selectedCam)){
            selectedCam = 0
            localStorage.setItem("selectedCam", 0)
        }
        //Create video element for camera output
        let videoElem = document.createElement('video')
	videoElem.id = "meals-scan-video"
        //Init scanner with this element
        let scanner = new Instascan.Scanner({ video: videoElem });
        scanner.addListener('scan', function (content) {
            console.info("Read QR content: "+content)
            $("#id_search")[0].value = content
            scanner.stop()
	    document.getElementById("meals-search").submit()
        });
        camerainput = document.getElementById("meals-scan-image")
        camerainput.classList.add("meals-inside-scan")
        //Append camera selector
        let selectCam = document.createElement("select")
	selectCam.classList.add("form-control")
    selectCam.classList.add("selected-camera-class")
        let optionsStr=""
        for(let i =0; i < cams.length; i++)
            optionsStr += "<option value='"+i+"'>" + (cams[i].name || "Camera "+i) + "</option>"
        selectCam.innerHTML=optionsStr
        camerainput.appendChild(selectCam)
        selectCam.value = ""+selectedCam
        //On selector change, we stop the scanner preview and change the camera
        selectCam.addEventListener("change", ()=>{
            let selectedCam = parseInt($(".selected-camera-class option:selected").val())
            localStorage.setItem("selectedCam", selectedCam)
            scanner.stop()
            scanner.start(cams[selectedCam])
        })
        //Then we append the video preview
        camerainput.appendChild(videoElem)

        //Start the scanner with the stored value
        scanner.start(cams[selectedCam])

    }

    return obj
})()

document.addEventListener("DOMContentLoaded", ()=>{
    if (Instascan.Camera == null){
	var t = setInterval(obj.initListeners(), 1000)
    }
    else{
	clearInterval(t)
	meals_webcam.initScanner()
    }
    meals_webcam.initListeners()
})
