var butts = document.getElementsByClassName("play");
for (var i = 0; i < butts.length; i++) {
   butts[i].addEventListener("click", playPause);
}

var butts = document.getElementsByClassName("pause");
for (var i = 0; i < butts.length; i++) {
   butts[i].style.display = "none";
   butts[i].addEventListener("click", playPause);
}
function playPause(e) {
   e = e || window.event;
   e = e.target || e.srcElement;
   var str = e.id;
   id = str.substring(3, str.length);
   video = document.getElementById("myvid_" + id);
   play = document.getElementById("pl_" + id);
   pause = document.getElementById("pa_" + id);
   progress = document.getElementById("pr_" + id)
   volume = document.getElementById("vo_" + id)
   timer = document.getElementById("ti_" + id)
   timerend = document.getElementById("te_" + id)
   volume.addEventListener('change', function (e) {
      video.volume = e.currentTarget.value / 100;
   });
   video.addEventListener('timeupdate', () => {
      progress.value = video.currentTime / video.duration;
      timer.innerHTML = calculateTime(video.currentTime);
      timerend.innerHTML = calculateTime(video.duration);
   });

   if (video.paused) {
      video.play();
      play.style.display = "none";
      pause.style.display = "inline";
   }
   else {
      video.pause();
      pause.style.display = "none";
      play.style.display = "inline";
   }
}
const calculateTime = (secs) => {
   const minutes = Math.floor(secs / 60);
   const seconds = Math.floor(secs % 60);
   const returnedSeconds = seconds < 10 ? `0${seconds}` : `${seconds}`;
   return `${minutes}:${returnedSeconds}`;
}
window.addEventListener("play", function(evt)
{
    if(window.$_currentlyPlaying && window.$_currentlyPlaying != evt.target)
    {
        window.$_currentlyPlaying.pause();
        evt.target=calculateTime(evt.target.currentTime=0);
        player_set=window.$_currentlyPlaying.id;
        newStr= player_set.replace('myvid_', '');
        document.getElementById('pl_'+newStr).style.display="inline";
        document.getElementById('pa_'+newStr).style.display="none";
        document.getElementById('pr_'+newStr).value=0;
        document.getElementById('ti_'+newStr).innerHTML="0:00";
    } 
    window.$_currentlyPlaying = evt.target;
}, true);