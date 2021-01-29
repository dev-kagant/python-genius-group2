[tweet link](https://awik.io/get-selected-text-and-cursor-position-javascript-to-show-popup-dialog/)

[selection stack overflow](https://stackoverflow.com/questions/43184603/select-text-highlight-selection-or-get-selection-value-react)

```
const article = document.getElementById("article");

// We could also add the  'touchend' event for touch devices, but since 
// most iOS/Android browsers already show a dialog when you select 
// text (often with a Share option) we'll skip that
article.addEventListener('mouseup', handlerFunction, false);

// Mouse up event handler function
function handlerFunction(event) {
    
    // If there is already a share dialog, remove it
    if (document.contains(document.getElementById("share-snippet"))) {
        document.getElementById("share-snippet").remove();
    }
    
    // Check if any text was selected
    if(window.getSelection().toString().length > 0) {

        // Get selected text and encode it
        const selection = encodeURIComponent(window.getSelection().toString()).replace(/[!'()*]/g, escape);
        
        // Find out how much (if any) user has scrolled
        var scrollTop = (window.pageYOffset !== undefined) ? window.pageYOffset : (document.documentElement || document.body.parentNode || document.body).scrollTop;
        
        // Get cursor position
        const posX = event.clientX - 110;
        const posY = event.clientY + 20 + scrollTop;
      
        // Create Twitter share URL
        const shareUrl = 'http://twitter.com/share?text='+selection+'&url=https://awik.io';
        
        // Append HTML to the body, create the "Tweet Selection" dialog
        document.body.insertAdjacentHTML('beforeend', '<div id="share-snippet" style="position: absolute; top: '+posY+'px; left: '+posX+'px;"><div class="speech-bubble"><div class="share-inside"><a href="javascript:void(0);" onClick=\'window.open(\"'+shareUrl+'\", \"\", \"menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=600,width=600\");\'>TWEET SELECTION</a></div></div></div>');
    }
}
```

Example:
[![Image from Gyazo](https://i.gyazo.com/8587be37e48a2bb9d69b222df9fa820f.png)](https://gyazo.com/8587be37e48a2bb9d69b222df9fa820f)