const play=document.querySelector('#play');
const pause=document.querySelector('#pause');
const video=document.querySelector('audio')[1];
const progres=document.querySelector('#progress');
const volume=document.querySelector("#volume");
const timer=document.querySelector("#timer");
const timerend=document.querySelector("#timerend");


pause.style.display="none";
play.addEventListener('click',playPause);
pause.addEventListener('click',playPause);
function playPause(){
   if (video[1].paused){
      video[1].play();
      play.style.display="none";
      pause.style.display="inline";
   }
   else{
      video[1].pause();
      pause.style.display="none";
      play.style.display="inline";
   }
}

video[1].addEventListener('timeupdate',()=>{
   progres.value=video.currentTime/video.duration;
});
volume[1].addEventListener('change',function(e){
   video.volume=e.currentTarget.value/100;
});

const calculateTime = (secs) => {
   const minutes = Math.floor(secs / 60);
   const seconds = Math.floor(secs % 60);
   const returnedSeconds = seconds < 10 ? `0${seconds}` : `${seconds}`;
   return `${minutes}:${returnedSeconds}`;
}
video[1].addEventListener('timeupdate',()=>{
   timer.innerHTML=calculateTime(video.currentTime);
});
video[1].addEventListener('timeupdate',()=>{
   timerend.innerHTML=calculateTime(video.duration);
});