var play=document.querySelector('#play');
var pause=document.querySelector('#pause');
var video=document.querySelector('audio');
var progres=document.querySelector('#progress');
var volume=document.querySelector("#volume");
var timer=document.querySelector("#timer");
var timerend=document.querySelector("#timerend");


pause.style.display="none";
play.addEventListener('click',playPause);
pause.addEventListener('click',playPause);
function playPause(){
   if (video.paused){
      video.play();
      play.style.display="none";
      pause.style.display="inline";
   }
   else{
      video.pause();
      pause.style.display="none";
      play.style.display="inline";
   }
}

video.addEventListener('timeupdate',function(this){
   progres.value=video.currentTime/video.duration;
});
volume.addEventListener('change',function(e){
   video.volume=e.currentTarget.value/100;
});

const calculateTime = (secs) => {
   const minutes = Math.floor(secs / 60);
   const seconds = Math.floor(secs % 60);
   const returnedSeconds = seconds < 10 ? `0${seconds}` : `${seconds}`;
   return `${minutes}:${returnedSeconds}`;
}
video.addEventListener('timeupdate',function(this){
   timer.innerHTML=calculateTime(video.currentTime);
});
video.addEventListener('timeupdate',function(this){
   timerend.innerHTML=calculateTime(video.duration);
});