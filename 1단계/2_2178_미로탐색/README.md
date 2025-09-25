https://www.acmicpc.net/problem/2178
<section id="description" class="problem-section">
    <div class="headline">
        <h2>문제</h2>
    </div>
    <div id="problem_description" class="problem-text">
        <p>N×M크기의 배열로 표현되는 미로가 있다.</p>
        <table class="table table-bordered" style="width:18%">
            <tbody>
                <tr>
                    <td style="width:3%">1</td>
                    <td style="width:3%">0</td>
                    <td style="width:3%">1</td>
                    <td style="width:3%">1</td>
                    <td style="width:3%">1</td>
                    <td style="width:3%">1</td>
                </tr>
                <tr>
                    <td>1</td>
                    <td>0</td>
                    <td>1</td>
                    <td>0</td>
                    <td>1</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>1</td>
                    <td>0</td>
                    <td>1</td>
                    <td>0</td>
                    <td>1</td>
                    <td>1</td>
                </tr>
                <tr>
                    <td>1</td>
                    <td>1</td>
                    <td>1</td>
                    <td>0</td>
                    <td>1</td>
                    <td>1</td>
                </tr>
            </tbody>
        </table>
        <p>미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.</p>
        <p>위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.</p>
    </div>
</section>

<section id="input" class="problem-section">
    <div class="headline">
        <h2>입력</h2>
    </div>
    <div id="problem_input" class="problem-text">
        <p>첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 <strong>붙어서</strong> 입력으로 주어진다.</p>
    </div>
</section>

<section id="output" class="problem-section">
    <div class="headline">
        <h2>출력</h2>
    </div>
    <div id="problem_output" class="problem-text">
        <p>첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.</p>
    </div>
</section>

<section id="sampleinput1">
    <div class="headline">
        <h2>예제 입력 1</h2>
    </div>
    <pre class="sampledata" id="sample-input-1">4 6
101111
101010
101011
111011
</pre>
</section>

<section id="sampleoutput1">
    <div class="headline">
        <h2>예제 출력 1</h2>
    </div>
    <pre class="sampledata" id="sample-output-1">15</pre>
</section>

<div class="row">
    <div class="col-md-6">
        <section id="sampleinput3">
            <div class="headline">
                <h2>예제 입력 3</h2>
            </div>
            <pre class="sampledata" id="sample-input-3">2 25
1011101110111011101110111
1110111011101110111011101
</pre>
        </section>
    </div>
    <div class="col-md-6">
        <section id="sampleoutput3">
            <div class="headline">
                <h2>예제 출력 3</h2>
            </div>
            <pre class="sampledata" id="sample-output-3">38
</pre>
        </section>
    </div>
</div>

<div class="row">
    <div class="col-md-6">
        <section id="sampleinput4">
            <div class="headline">
                <h2>예제 입력 4</h2>
            </div>
            <pre class="sampledata" id="sample-input-4">7 7
1011111
1110001
1000001
1000001
1000001
1000001
1111111
</pre>
        </section>
    </div>
    <div class="col-md-6">
        <section id="sampleoutput4">
            <div class="headline">
                <h2>예제 출력 4</h2>
            </div>
            <pre class="sampledata" id="sample-output-4">13
</pre>
        </section>
    </div>
</div>

<section id="source">
    <div class="headline">
        <h2>출처</h2>
    </div>
    <ul>
        <li>데이터를 추가한 사람:&nbsp;<a>djm03178</a>, <a>jh05013</a>, <a>poia0304</a>, <a>sait2000</a></li>
    </ul>
</section>

<section id="problem_tags">
    <div class="headline">
        <h2>알고리즘 분류</h2>
    </div>
    <ul class="spoiler-list">
        <li>
            <a class="spoiler-link">그래프 이론</a>
        </li>
        <li>
            <a class="spoiler-link">그래프 탐색</a>
        </li>
        <li>
            <a class="spoiler-link">너비 우선 탐색</a>
        </li>
        <li>
            <a class="spoiler-link">격자 그래프</a>
        </li>
    </ul>
</section>
