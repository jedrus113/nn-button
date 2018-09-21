from django.http import HttpResponse

from nn import ai_tree


def get_page(request):
    return HttpResponse("""
    <html><head><title>AI Button Validator</title></head>
    <body>
        <div id='message'>Mess</div>
        <button id='bttn' text="Bttn" />
    <script>
        var bx1, by1, bx2, by2;

        var bttn = document.getElementById('bttn');
        bttn.style.position = "absolute";
        
        var bttn_m = "";
        var url = '/req'
        
        set_bttn = function(x1,y1,x2,y2){
            bttn.style.top = x1;
            bttn.style.left = y1;
            bttn.style.width = y2 - y1;
            bttn.style.height = x2 - x1;

            bttn_m = "&bx1=" +x1+ "&by1=" +y1+ "&bx2=" +x2+ "&by2=" +y2;
            bx1 = x1;
            by1 = y1;
            bx2 = x2;
            by2 = y2;
        }

        set_bttn(200,200, 400,400)

        fn = function(event){
            var request = new XMLHttpRequest();

            el = document.getElementById('message');
            let m = "?x=" + event.clientX;
            m = m + "&y=" + event.clientY;
            request.open('GET',  url + m + bttn_m, false);
            request.send();
            el.innerHTML = request.responseText;
        }
        document.body.addEventListener('click', fn, true);
    </script>
    </body></html>
            """)


def ai_response(request):
    odp = ai_tree.predict(**request.GET)
    return HttpResponse(odp)
