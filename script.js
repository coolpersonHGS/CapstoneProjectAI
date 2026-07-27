 const downloadbutton = document.getElementById("download_button");

 downloadbutton.onclick = function ()
 {
    const link = document.createElement('a');
    link.href = "RedderreInstall.dmg";
    link.download = "result";
    document.body.appendChild(link);
    link.click();
    link.remove();
 };