navigator.mediaDevices.getUserMedia({
        audio: true
    })
    .then(stream => {
        handlerFunction(stream)
    })


function handlerFunction(stream) {
    let audioChunks = [];
    rec = new MediaRecorder(stream);
    rec.ondataavailable = (e) => {
        audioChunks.push(e.data);
        if (rec.state == "inactive") {
            let blob = new Blob(audioChunks, {
                type: 'audio/mpeg-3'
            });
            recordedAudio.src = URL.createObjectURL(blob);
            recordedAudio.controls = true;
            recordedAudio.autoplay = true;
            sendData(blob)
        }
    }
}

function sendData(data) {
    let fd = new FormData();
    fd.append("audio", data);
    $.ajax({
        url: '/record/send/',
        type: 'POST',
        data: fd,
        async: true,
        contentType: false,
        processData: false,
    }).done((e) => {
        console.log(e);
    });
}

record.onclick = (e) => {
    console.log('Record was clicked')
    record.disabled = true;
    stopRecord.disabled = false;
    audioChunks = [];
    rec.start();
}

stopRecord.onclick = (e) => {
    console.log("Stop was clicked")
    record.disabled = false;
    stop.disabled = true;
    rec.stop();
}