https://www.acmicpc.net/problem/9205
<div id="problem-body" class="">
    <div class="col-md-12">
        <section id="description" class="problem-section">
            <div class="headline">
                <h2>문제</h2>
            </div>
            <div id="problem_description" class="problem-text">
                <p>송도에 사는 상근이와 친구들은 송도에서 열리는 펜타포트 락 페스티벌에 가려고 한다. 올해는 맥주를 마시면서 걸어가기로 했다. 출발은 상근이네 집에서 하고, 맥주 한 박스를 들고 출발한다. 맥주 한 박스에는 맥주가 20개 들어있다. 목이 마르면 안되기 때문에 50미터에 한 병씩 마시려고 한다.&nbsp;즉, 50미터를 가려면 그 직전에 맥주 한 병을 마셔야 한다.</p>
                <p>상근이의 집에서 페스티벌이 열리는&nbsp;곳은 매우 먼 거리이다. 따라서, 맥주를 더 구매해야 할 수도 있다. 미리 인터넷으로 조사를 해보니 다행히도 맥주를 파는 편의점이 있다. 편의점에 들렸을 때, 빈 병은 버리고 새 맥주 병을 살 수 있다. 하지만, 박스에 들어있는 맥주는 20병을 넘을 수 없다.&nbsp;편의점을 나선 직후에도 50미터를 가기 전에 맥주 한 병을 마셔야 한다.</p>
                <p>편의점, 상근이네 집, 펜타포트 락 페스티벌의 좌표가 주어진다. 상근이와 친구들이 행복하게 페스티벌에 도착할 수 있는지 구하는 프로그램을 작성하시오.</p>
            </div>
        </section>
    </div>
    <div class="col-md-12">
        <section id="input" class="problem-section">
            <div class="headline">
                <h2>입력</h2>
            </div>
            <div id="problem_input" class="problem-text">
                <p>첫째 줄에 테스트 케이스의 개수 t가 주어진다. (t ≤ 50)</p>
                <p>각 테스트 케이스의 첫째 줄에는 맥주를 파는 편의점의 개수 n이 주어진다. (0 ≤ n ≤ 100).</p>
                <p>다음 n+2개 줄에는 상근이네 집, 편의점, 펜타포트 락 페스티벌 좌표가 주어진다. 각 좌표는 두 정수 x와 y로 이루어져 있다. (두 값 모두 미터, -32768 ≤ x, y ≤ 32767)</p>
                <p>송도는 직사각형 모양으로 생긴 도시이다. 두 좌표 사이의 거리는 x 좌표의 차이 + y 좌표의 차이 이다. (맨해튼 거리)</p>
            </div>
        </section>
    </div>
    <div class="col-md-12">
        <section id="output" class="problem-section">
            <div class="headline">
                <h2>출력</h2>
            </div>
            <div id="problem_output" class="problem-text">
                <p>각 테스트 케이스에 대해서 상근이와 친구들이 행복하게 페스티벌에 갈 수 있으면 "happy", 중간에 맥주가 바닥나서 더 이동할 수 없으면 "sad"를 출력한다.&nbsp;</p>
            </div>
        </section>
    </div>
    <div class="col-md-12">
        <section id="limit" style="display:none;" class="problem-section">
            <div class="headline">
                <h2>제한</h2>
            </div>
            <div id="problem_limit" class="problem-text">
            </div>
        </section>
    </div>
    <div class="col-md-12">
        <div class="row">
            <div class="col-md-6">
                <section id="sampleinput1">
                    <div class="headline">
                        <h2>예제 입력 1</h2>
                    </div>
                    <pre class="sampledata" id="sample-input-1">2
2
0 0
1000 0
1000 1000
2000 1000
2
0 0
1000 0
2000 1000
2000 2000
</pre>
                </section>
            </div>
            <div class="col-md-6">
                <section id="sampleoutput1">
                    <div class="headline">
                        <h2>예제 출력 1</h2>
                    </div>
                    <pre class="sampledata" id="sample-output-1">happy
sad
</pre>
                </section>
            </div>
        </div>
    </div>
    <div class="col-md-12">
        <section id="hint" style="display: none;" class="problem-section">
            <div class="headline">
                <h2>힌트</h2>
            </div>
            <div id="problem_hint" class="problem-text">
            </div>
        </section>
    </div>
    <div style="display: none;">
        <div id="problem-lang-base64">W3sicHJvYmxlbV9pZCI6IjkyMDUiLCJwcm9ibGVtX2xhbmciOiIwIiwidGl0bGUiOiJcdWI5ZTVcdWM4ZmMgXHViOWM4XHVjMmRjXHViYTc0XHVjMTFjIFx1YWM3OFx1YzViNFx1YWMwMFx1YWUzMCIsImRlc2NyaXB0aW9uIjoiPHA+XHVjMWExXHViM2M0XHVjNWQwIFx1YzBhY1x1YjI5NCBcdWMwYzFcdWFkZmNcdWM3NzRcdWM2NDAgXHVjZTVjXHVhZDZjXHViNGU0XHVjNzQwIFx1YzFhMVx1YjNjNFx1YzVkMFx1YzExYyBcdWM1ZjRcdWI5YWNcdWIyOTQgXHVkMzljXHVkMGMwXHVkM2VjXHVkMmI4IFx1Yjc3ZCBcdWQzOThcdWMyYTRcdWQyZjBcdWJjOGNcdWM1ZDAgXHVhYzAwXHViODI0XHVhY2UwIFx1ZDU1Y1x1YjJlNC4gXHVjNjJjXHVkNTc0XHViMjk0IFx1YjllNVx1YzhmY1x1Yjk3YyBcdWI5YzhcdWMyZGNcdWJhNzRcdWMxMWMgXHVhYzc4XHVjNWI0XHVhYzAwXHVhZTMwXHViODVjIFx1ZDU4OFx1YjJlNC4gXHVjZDljXHViYzFjXHVjNzQwIFx1YzBjMVx1YWRmY1x1Yzc3NFx1YjEyNCBcdWM5ZDFcdWM1ZDBcdWMxMWMgXHVkNTU4XHVhY2UwLCBcdWI5ZTVcdWM4ZmMgXHVkNTVjIFx1YmMxNVx1YzJhNFx1Yjk3YyBcdWI0ZTRcdWFjZTAgXHVjZDljXHViYzFjXHVkNTVjXHViMmU0LiBcdWI5ZTVcdWM4ZmMgXHVkNTVjIFx1YmMxNVx1YzJhNFx1YzVkMFx1YjI5NCBcdWI5ZTVcdWM4ZmNcdWFjMDAgMjBcdWFjMWMgXHViNGU0XHVjNWI0XHVjNzg4XHViMmU0LiBcdWJhYTlcdWM3NzQgXHViOWM4XHViOTc0XHViYTc0IFx1YzU0OFx1YjQxOFx1YWUzMCBcdWI1NGNcdWJiMzhcdWM1ZDAgNTBcdWJiZjhcdWQxMzBcdWM1ZDAgXHVkNTVjIFx1YmNkMVx1YzUyOSBcdWI5YzhcdWMyZGNcdWI4MjRcdWFjZTAgXHVkNTVjXHViMmU0LiZuYnNwO1x1Yzk4OSwgNTBcdWJiZjhcdWQxMzBcdWI5N2MgXHVhYzAwXHViODI0XHViYTc0IFx1YWRmOCBcdWM5YzFcdWM4MDRcdWM1ZDAgXHViOWU1XHVjOGZjIFx1ZDU1YyBcdWJjZDFcdWM3NDQgXHViOWM4XHVjMTU0XHVjNTdjIFx1ZDU1Y1x1YjJlNC48XC9wPlxyXG5cclxuPHA+XHVjMGMxXHVhZGZjXHVjNzc0XHVjNzU4IFx1YzlkMVx1YzVkMFx1YzExYyBcdWQzOThcdWMyYTRcdWQyZjBcdWJjOGNcdWM3NzQgXHVjNWY0XHViOWFjXHViMjk0Jm5ic3A7XHVhY2YzXHVjNzQwIFx1YjllNFx1YzZiMCBcdWJhM2MgXHVhYzcwXHViOWFjXHVjNzc0XHViMmU0LiBcdWI1MzBcdWI3N2NcdWMxMWMsIFx1YjllNVx1YzhmY1x1Yjk3YyBcdWIzNTQgXHVhZDZjXHViOWU0XHVkNTc0XHVjNTdjIFx1ZDU2MCBcdWMyMThcdWIzYzQgXHVjNzg4XHViMmU0LiBcdWJiZjhcdWI5YWMgXHVjNzc4XHVkMTMwXHViMTM3XHVjNzNjXHViODVjIFx1Yzg3MFx1YzBhY1x1Yjk3YyBcdWQ1NzRcdWJjZjRcdWIyYzggXHViMmU0XHVkNTg5XHVkNzg4XHViM2M0IFx1YjllNVx1YzhmY1x1Yjk3YyBcdWQzMGNcdWIyOTQgXHVkM2I4XHVjNzU4XHVjODEwXHVjNzc0IFx1Yzc4OFx1YjJlNC4gXHVkM2I4XHVjNzU4XHVjODEwXHVjNWQwIFx1YjRlNFx1YjgzOFx1Yzc0NCBcdWI1NGMsIFx1YmU0OCBcdWJjZDFcdWM3NDAgXHViYzg0XHViOWFjXHVhY2UwIFx1YzBjOCBcdWI5ZTVcdWM4ZmMgXHViY2QxXHVjNzQ0IFx1YzBiNCBcdWMyMTggXHVjNzg4XHViMmU0LiBcdWQ1NThcdWM5YzBcdWI5Y2MsIFx1YmMxNVx1YzJhNFx1YzVkMCBcdWI0ZTRcdWM1YjRcdWM3ODhcdWIyOTQgXHViOWU1XHVjOGZjXHViMjk0IDIwXHViY2QxXHVjNzQ0IFx1YjExOFx1Yzc0NCBcdWMyMTggXHVjNWM2XHViMmU0LiZuYnNwO1x1ZDNiOFx1Yzc1OFx1YzgxMFx1Yzc0NCBcdWIwOThcdWMxMjAgXHVjOWMxXHVkNmM0XHVjNWQwXHViM2M0IDUwXHViYmY4XHVkMTMwXHViOTdjIFx1YWMwMFx1YWUzMCBcdWM4MDRcdWM1ZDAgXHViOWU1XHVjOGZjIFx1ZDU1YyBcdWJjZDFcdWM3NDQgXHViOWM4XHVjMTU0XHVjNTdjIFx1ZDU1Y1x1YjJlNC48XC9wPlxyXG5cclxuPHA+XHVkM2I4XHVjNzU4XHVjODEwLCBcdWMwYzFcdWFkZmNcdWM3NzRcdWIxMjQgXHVjOWQxLCBcdWQzOWNcdWQwYzBcdWQzZWNcdWQyYjggXHViNzdkIFx1ZDM5OFx1YzJhNFx1ZDJmMFx1YmM4Y1x1Yzc1OCBcdWM4OGNcdWQ0NWNcdWFjMDAgXHVjOGZjXHVjNWI0XHVjOWM0XHViMmU0LiBcdWMwYzFcdWFkZmNcdWM3NzRcdWM2NDAgXHVjZTVjXHVhZDZjXHViNGU0XHVjNzc0IFx1ZDU4OVx1YmNmNVx1ZDU1OFx1YWM4YyBcdWQzOThcdWMyYTRcdWQyZjBcdWJjOGNcdWM1ZDAgXHViM2M0XHVjYzI5XHVkNTYwIFx1YzIxOCBcdWM3ODhcdWIyOTRcdWM5YzAgXHVhZDZjXHVkNTU4XHViMjk0IFx1ZDUwNFx1Yjg1Y1x1YWRmOFx1YjdhOFx1Yzc0NCBcdWM3OTFcdWMxMzFcdWQ1NThcdWMyZGNcdWM2MjQuPFwvcD5cclxuIiwiaW5wdXQiOiI8cD5cdWNjYWJcdWM5ZjggXHVjOTA0XHVjNWQwIFx1ZDE0Y1x1YzJhNFx1ZDJiOCBcdWNmMDBcdWM3NzRcdWMyYTRcdWM3NTggXHVhYzFjXHVjMjE4IHRcdWFjMDAgXHVjOGZjXHVjNWI0XHVjOWM0XHViMmU0LiAodCAmbGU7IDUwKTxcL3A+XHJcblxyXG48cD5cdWFjMDEgXHVkMTRjXHVjMmE0XHVkMmI4IFx1Y2YwMFx1Yzc3NFx1YzJhNFx1Yzc1OCBcdWNjYWJcdWM5ZjggXHVjOTA0XHVjNWQwXHViMjk0IFx1YjllNVx1YzhmY1x1Yjk3YyBcdWQzMGNcdWIyOTQgXHVkM2I4XHVjNzU4XHVjODEwXHVjNzU4IFx1YWMxY1x1YzIxOCBuXHVjNzc0IFx1YzhmY1x1YzViNFx1YzljNFx1YjJlNC4gKDAgJmxlOyBuICZsZTsgMTAwKS48XC9wPlxyXG5cclxuPHA+XHViMmU0XHVjNzRjIG4rMlx1YWMxYyBcdWM5MDRcdWM1ZDBcdWIyOTQgXHVjMGMxXHVhZGZjXHVjNzc0XHViMTI0IFx1YzlkMSwgXHVkM2I4XHVjNzU4XHVjODEwLCBcdWQzOWNcdWQwYzBcdWQzZWNcdWQyYjggXHViNzdkIFx1ZDM5OFx1YzJhNFx1ZDJmMFx1YmM4YyBcdWM4OGNcdWQ0NWNcdWFjMDAgXHVjOGZjXHVjNWI0XHVjOWM0XHViMmU0LiBcdWFjMDEgXHVjODhjXHVkNDVjXHViMjk0IFx1YjQ1MCBcdWM4MTVcdWMyMTggeFx1YzY0MCB5XHViODVjIFx1Yzc3NFx1YjhlOFx1YzViNFx1YzgzOCBcdWM3ODhcdWIyZTQuIChcdWI0NTAgXHVhYzEyIFx1YmFhOFx1YjQ1MCBcdWJiZjhcdWQxMzAsIC0zMjc2OCAmbGU7IHgsIHkgJmxlOyAzMjc2Nyk8XC9wPlxyXG5cclxuPHA+XHVjMWExXHViM2M0XHViMjk0IFx1YzljMVx1YzBhY1x1YWMwMVx1ZDYxNSBcdWJhYThcdWM1OTFcdWM3M2NcdWI4NWMgXHVjMGRkXHVhZTM0IFx1YjNjNFx1YzJkY1x1Yzc3NFx1YjJlNC4gXHViNDUwIFx1Yzg4Y1x1ZDQ1YyBcdWMwYWNcdWM3NzRcdWM3NTggXHVhYzcwXHViOWFjXHViMjk0IHggXHVjODhjXHVkNDVjXHVjNzU4IFx1Y2MyOFx1Yzc3NCArIHkgXHVjODhjXHVkNDVjXHVjNzU4IFx1Y2MyOFx1Yzc3NCBcdWM3NzRcdWIyZTQuIChcdWI5ZThcdWQ1NzRcdWQyYmMgXHVhYzcwXHViOWFjKTxcL3A+XHJcbiIsIm91dHB1dCI6IjxwPlx1YWMwMSBcdWQxNGNcdWMyYTRcdWQyYjggXHVjZjAwXHVjNzc0XHVjMmE0XHVjNWQwIFx1YjMwMFx1ZDU3NFx1YzExYyBcdWMwYzFcdWFkZmNcdWM3NzRcdWM2NDAgXHVjZTVjXHVhZDZjXHViNGU0XHVjNzc0IFx1ZDU4OVx1YmNmNVx1ZDU1OFx1YWM4YyBcdWQzOThcdWMyYTRcdWQyZjBcdWJjOGNcdWM1ZDAgXHVhYzA4IFx1YzIxOCBcdWM3ODhcdWM3M2NcdWJhNzQgJnF1b3Q7aGFwcHkmcXVvdDssIFx1YzkxMVx1YWMwNFx1YzVkMCBcdWI5ZTVcdWM4ZmNcdWFjMDAgXHViYzE0XHViMmU1XHViMDk4XHVjMTFjIFx1YjM1NCBcdWM3NzRcdWIzZDlcdWQ1NjAgXHVjMjE4IFx1YzVjNlx1YzczY1x1YmE3NCAmcXVvdDtzYWQmcXVvdDtcdWI5N2MgXHVjZDljXHViODI1XHVkNTVjXHViMmU0LiZuYnNwOzxcL3A+XHJcbiIsImhpbnQiOiIiLCJvcmlnaW5hbCI6IjAiLCJodG1sX3RpdGxlIjoiMCIsInByb2JsZW1fbGFuZ190Y29kZSI6IktvcmVhbiJ9LHsicHJvYmxlbV9pZCI6IjkyMDUiLCJwcm9ibGVtX2xhbmciOiIxIiwidGl0bGUiOiJLYXN0ZW5sYXVmIiwiZGVzY3JpcHRpb24iOiI8cD5PbmNlIGV2ZXJ5IHllYXIsIEpvIGFuZCBoaXMgZnJpZW5kcyB3YW50IHRvIHZpc2l0IHRoZSBsb2NhbCBmYWlyIGluIEVybGFuZ2VuLCBjYWxsZWQgQmVyZ2tpcmNod2VpaC4gVGhpcyB5ZWFyLCB0aGV5IHdhbnQgdG8gbWFrZSBhIEthc3RlbmxhdWYgKGJveCBydW4pLiBUaGV5IHN0YXJ0IGF0IEpvJnJzcXVvO3MgaG9tZSwgYW5kIGhhdmUgb25lIGJveCAoS2FzdGVuKSBvZiBiZWVyICh3aXRoIHR3ZW50eSBib3R0bGVzKS4gQXMgdGhleSBhcmUgdmVyeSB0aGlyc3R5LCB0aGV5IGRyaW5rIG9uZSBib3R0bGUgb2YgYmVlciBldmVyeSA1MCBtZXRyZXMuJm5ic3A7SW4gb3RoZXIgd29yZHMsIGluIG9yZGVyIHRvIHdhbGsgNTAgbWV0cmVzLCB0aGV5IHNob3VsZCBkcmluayBhIGJvdHRsZSByaWdodCBiZWZvcmUgdGhhdC48XC9wPlxyXG5cclxuPHA+QXMgdGhlIHdheSBmcm9tIEpvJnJzcXVvO3MgaG9tZSB0byB0aGUgQmVyZ2tpcmNod2VpaCBpcyBwcmV0dHkgbG9uZywgdGhleSBuZWVkIG1vcmUgYmVlciB0aGFuIHRoZXkgaGF2ZSBpbml0aWFsbHkuIEZvcnR1bmF0ZWx5LCB0aGVyZSBhcmUgc3RvcmVzIHNlbGxpbmcgYmVlciBvbiB0aGUgd2F5LiBXaGVuIHRoZXkgdmlzaXQgYSBzdG9yZSwgdGhleSBjYW4gZHJvcCB0aGVpciBlbXB0eSBib3R0bGVzIGFuZCBidXkgbmV3IGJvdHRsZXMsIGJ1dCB0aGVpciB0b3RhbCBudW1iZXIgb2YgZnVsbCBib3R0bGVzIHdpbGwgbm90IGJlIG1vcmUgdGhhbiB0d2VudHkgKGJlY2F1c2UgdGhleSBhcmUgdG9vIGxhenkgdG8gY2FycnkgbW9yZSB0aGFuIG9uZSBmdWxsIGJveCkuJm5ic3A7QWZ0ZXIgbGVhdmluZyB0aGUgc3RvcmUsIHRoZXkgc2hvdWxkIGRyaW5rIGEgYm90dGxlIGJlZm9yZSBtb3ZpbmcgNTAgbWV0cmVzLjxcL3A+XHJcblxyXG48cD5Zb3UgYXJlIGdpdmVuIHRoZSBjb29yZGluYXRlcyBvZiB0aGUgc3RvcmVzLCBvZiBKbyZyc3F1bztzIGhvbWUgYW5kIG9mIHRoZSBsb2NhdGlvbiBvZiB0aGUgQmVyZ2tpcmNod2VpaC48XC9wPlxyXG5cclxuPHA+V3JpdGUgYSBwcm9ncmFtIHRvIGRldGVybWluZSB3aGV0aGVyIEpvIGFuZCBoaXMgZnJpZW5kcyBjYW4gaGFwcGlseSByZWFjaCB0aGUgQmVyZ2tpcmNod2VpaCwgb3Igd2hldGhlciB0aGV5IHdpbGwgcnVuIG91dCBvZiBiZWVyIG9uIHRoZSB3YXkuPFwvcD5cclxuIiwiaW5wdXQiOiI8cD5JbnB1dCBzdGFydHMgd2l0aCBvbmUgbGluZSBjb250YWluaW5nIHRoZSBudW1iZXIgb2YgdGVzdCBjYXNlcyB0ICh0ICZsZTsgNTApLjxcL3A+XHJcblxyXG48cD5FYWNoIHRlc3QgY2FzZSBzdGFydHMgd2l0aCBvbmUgbGluZSwgY29udGFpbmluZyB0aGUgbnVtYmVyIG4gb2Ygc3RvcmVzIHNlbGxpbmcgYmVlciAod2l0aCAwICZsZTsgbiAmbGU7IDEwMCkuPFwvcD5cclxuXHJcbjxwPlRoZSBuZXh0IG4gKyAyIGxpbmVzIGNvaW50YWluIChpbiB0aGlzIG9yZGVyKSB0aGUgbG9jYXRpb24gb2YgSm8mcnNxdW87cyBob21lLCBvZiB0aGUgc3RvcmVzLCBhbmQgb2YgdGhlIEJlcmdraXJjaHdlaWguIFRoZSBsb2NhdGlvbiBpcyBnaXZlbiB3aXRoIHR3byBpbnRlZ2VyIGNvb3JkaW5hdGVzIHggYW5kIHksIChib3RoIGluIG1ldGVycywgLTMyNzY4ICZsZTsgeCwgeSAmbGU7IDMyNzY3KS48XC9wPlxyXG5cclxuPHA+QXMgRXJsYW5nZW4gaXMgYSByZWN0YW5ndWxhcmx5IGxhaWQgb3V0IGNpdHksIHRoZSBkaXN0YW5jZSBiZXR3ZWVuIHR3byBsb2NhdGlvbnMgaXMgdGhlIGRpZmZlcmVuY2Ugb2YgdGhlIGZpcnN0IGNvb3JkaW5hdGUgcGx1cyB0aGUgZGlmZmVyZW5jZSBvZiB0aGUgc2Vjb25kIGNvb3JkaW5hdGUgKGFsc28gY2FsbGVkIE1hbmhhdHRhbi1NZXRyaWMpLjxcL3A+XHJcbiIsIm91dHB1dCI6IjxwPkZvciBlYWNoIHRlc3QgY2FzZSBwcmludCBvbmUgbGluZSwgY29udGFpbmluZyBlaXRoZXIgJmxkcXVvO2hhcHB5JnJkcXVvOyAoaWYgSm8gYW5kIGhpcyBmcmllbmRzIGNhbiBoYXBwaWx5IHJlYWNoIHRoZSBCZXJna2lyY2h3ZWloKSwgb3IgJmxkcXVvO3NhZCZyZHF1bzsgKGlmIHRoZXkgd2lsbCBub3QgcmVhY2ggdGhlJm5ic3A7QmVyZ2tpcmNod2VpaCBiZWNhdXNlIHRoZXkmbmJzcDtydW4gb3V0IG9mIGJlZXIuKS48XC9wPlxyXG4iLCJoaW50IjoiIiwib3JpZ2luYWwiOiIxIiwiaHRtbF90aXRsZSI6IjAiLCJwcm9ibGVtX2xhbmdfdGNvZGUiOiJFbmdsaXNoIn1d</div>
    </div>
</div>