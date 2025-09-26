<div id="problem-body" class="">
    <div class="col-md-12">
        <section id="description" class="problem-section">
            <div class="headline">
                <h2>문제</h2>
            </div>
            <div id="problem_description" class="problem-text">
                <p>스타트링크에서 판매하는 어린이용 장난감 중에서 가장 인기가 많은 제품은 구슬 탈출이다. 구슬 탈출은 직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼내는 게임이다.</p>
                <p>보드의 세로 크기는 N, 가로 크기는 M이고, 편의상 1×1크기의 칸으로 나누어져 있다. 가장 바깥 행과 열은 모두 막혀져 있고, 보드에는 구멍이 하나 있다. 빨간 구슬과 파란 구슬의 크기는 보드에서 1×1크기의 칸을 가득 채우는 사이즈이고, 각각 하나씩 들어가 있다. 게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다. 이때, 파란 구슬이 구멍에 들어가면 안 된다.</p>
                <p>이때, 구슬을 손으로 건드릴 수는 없고, 중력을 이용해서 이리 저리 굴려야 한다. 왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기와 같은 네 가지 동작이 가능하다.</p>
                <p>각각의 동작에서 공은 동시에 움직인다. 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다.&nbsp;빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다. 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다. 또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다.&nbsp;기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.</p>
                <p>보드의 상태가 주어졌을 때, 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 프로그램을 작성하시오.</p>
            </div>
        </section>
    </div>
    <div class="col-md-12">
        <section id="input" class="problem-section">
            <div class="headline">
                <h2>입력</h2>
            </div>
            <div id="problem_input" class="problem-text">
                <p>첫 번째 줄에는 보드의 세로, 가로 크기를 의미하는 두 정수 N, M (3 ≤ N, M ≤ 10)이 주어진다. 다음 N개의 줄에 보드의 모양을 나타내는 길이 M의 문자열이 주어진다. 이 문자열은 '<code>.</code>', '<code>#</code>', '<code>O</code>', '<code>R</code>', '<code>B</code>' 로&nbsp;이루어져 있다. '<code>.</code>'은 빈 칸을 의미하고, '<code>#</code>'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며, '<code>O</code>'는 구멍의 위치를 의미한다. '<code>R</code>'은 빨간 구슬의 위치, '<code>B</code>'는 파란 구슬의 위치이다.</p>
                <p>입력되는 모든 보드의 가장자리에는 모두 '<code>#</code>'이 있다. 구멍의 개수는 한 개 이며, 빨간 구슬과 파란 구슬은 항상 1개가 주어진다.</p>
            </div>
        </section>
    </div>
    <div class="col-md-12">
        <section id="output" class="problem-section">
            <div class="headline">
                <h2>출력</h2>
            </div>
            <div id="problem_output" class="problem-text">
                <p>최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 출력한다.&nbsp;만약, 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1을 출력한다.</p>
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
                        <h2>예제 입력 1
                        </h2>
                    </div>
                    <pre class="sampledata" id="sample-input-1">5 5
#####
#..B#
#.#.#
#RO.#
#####
</pre>
                </section>
            </div>
            <div class="col-md-6">
                <section id="sampleoutput1">
                    <div class="headline">
                        <h2>예제 출력 1
                        </h2>
                    </div>
                    <pre class="sampledata" id="sample-output-1">1
</pre>
                </section>
            </div>
        </div>
    </div>
    <div class="col-md-12">
        <div class="row">
            <div class="col-md-6">
                <section id="sampleinput2">
                    <div class="headline">
                        <h2>예제 입력 2
                        </h2>
                    </div>
                    <pre class="sampledata" id="sample-input-2">7 7
#######
#...RB#
#.#####
#.....#
#####.#
#O....#
#######
</pre>
                </section>
            </div>
            <div class="col-md-6">
                <section id="sampleoutput2">
                    <div class="headline">
                        <h2>예제 출력 2
                        </h2>
                    </div>
                    <pre class="sampledata" id="sample-output-2">5
</pre>
                </section>
            </div>
        </div>
    </div>
    <div class="col-md-12">
        <div class="row">
            <div class="col-md-6">
                <section id="sampleinput3">
                    <div class="headline">
                        <h2>예제 입력 3
                        </h2>
                    </div>
                    <pre class="sampledata" id="sample-input-3">7 7
#######
#..R#B#
#.#####
#.....#
#####.#
#O....#
#######
</pre>
                </section>
            </div>
            <div class="col-md-6">
                <section id="sampleoutput3">
                    <div class="headline">
                        <h2>예제 출력 3
                        </h2>
                    </div>
                    <pre class="sampledata" id="sample-output-3">5
</pre>
                </section>
            </div>
        </div>
    </div>
    <div class="col-md-12">
        <div class="row">
            <div class="col-md-6">
                <section id="sampleinput4">
                    <div class="headline">
                        <h2>예제 입력 4
                        </h2>
                    </div>
                    <pre class="sampledata" id="sample-input-4">10 10
##########
#R#...##B#
#...#.##.#
#####.##.#
#......#.#
#.######.#
#.#....#.#
#.#.#.#..#
#...#.O#.#
##########
</pre>
                </section>
            </div>
            <div class="col-md-6">
                <section id="sampleoutput4">
                    <div class="headline">
                        <h2>예제 출력 4
                        </h2>
                    </div>
                    <pre class="sampledata" id="sample-output-4">-1
</pre>
                </section>
            </div>
        </div>
    </div>
    <div class="col-md-12">
        <div class="row">
            <div class="col-md-6">
                <section id="sampleinput5">
                    <div class="headline">
                        <h2>예제 입력 5
                        </h2>
                    </div>
                    <pre class="sampledata" id="sample-input-5">3 7
#######
#R.O.B#
#######
</pre>
                </section>
            </div>
            <div class="col-md-6">
                <section id="sampleoutput5">
                    <div class="headline">
                        <h2>예제 출력 5
                        </h2>
                    </div>
                    <pre class="sampledata" id="sample-output-5">1
</pre>
                </section>
            </div>
        </div>
    </div>
    <div class="col-md-12">
        <div class="row">
            <div class="col-md-6">
                <section id="sampleinput6">
                    <div class="headline">
                        <h2>예제 입력 6
                        </h2>
                    </div>
                    <pre class="sampledata" id="sample-input-6">10 10
##########
#R#...##B#
#...#.##.#
#####.##.#
#......#.#
#.######.#
#.#....#.#
#.#.##...#
#O..#....#
##########
</pre>
                </section>
            </div>
            <div class="col-md-6">
                <section id="sampleoutput6">
                    <div class="headline">
                        <h2>예제 출력 6
                        </h2>
                    </div>
                    <pre class="sampledata" id="sample-output-6">7
</pre>
                </section>
            </div>
        </div>
    </div>
    <div class="col-md-12">
        <div class="row">
            <div class="col-md-6">
                <section id="sampleinput7">
                    <div class="headline">
                        <h2>예제 입력 7
                        </h2>
                    </div>
                    <pre class="sampledata" id="sample-input-7">3 10
##########
#.O....RB#
##########
</pre>
                </section>
            </div>
            <div class="col-md-6">
                <section id="sampleoutput7">
                    <div class="headline">
                        <h2>예제 출력 7
                        </h2>
                    </div>
                    <pre class="sampledata" id="sample-output-7">-1
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
</div>