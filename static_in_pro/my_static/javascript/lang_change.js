
        var counter = 0;

        function changeText()
        {
        var quotes = new Array();

        quotes[0] = "Hello,";
        quotes[1] = "Hallo,";
        quotes[2] = "Hola,";
        quotes[3] = "नमस्ते,";
        quotes[4] = "Aloha,";
        quotes[5] = "你好,";
        quotes[6] = "こんにちは,";
        if (counter > 6)
            {
            counter = 0;
            }

        document.getElementById("textslide").innerHTML = quotes[counter];

        setTimeout(function(){changeText()},2000);
        counter ++;
        }
