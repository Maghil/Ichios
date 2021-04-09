var span = document.getElementsByClassName("close")[0];
    function showmdl(val) {
      var str =val;
      file = str.substring(3,str.length);
      name = document.getElementById("tt_"+file).innerHTML;
      document.getElementById("retxt").value="";
      document.getElementById("nmtxt").value=name;
      document.getElementById("hvtxt").value=file;
      var modal = document.getElementById("myModal");
      modal.style.display = "block";
    }
    span.onclick = function() {
      cancelbt();
    }
    function cancelbt()
    {
      var modal = document.getElementById("myModal");
      modal.style.display="none";
    }
    window.onclick = function(event) {
      var modal = document.getElementById("myModal");
      if (event.target == modal) {
        modal.style.display = "none";
      }
}



