https://www.acmicpc.net/problem/14503
<div id="problem-body" class="">
    <div class="col-md-12">
        <section id="description" class="problem-section">
            <div class="headline">
                <h2>문제</h2>
            </div>
            <div id="problem_description" class="problem-text">
                <p>로봇 청소기와 방의 상태가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.</p>
                <p>로봇 청소기가 있는 방은 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                        <mjx-math class="MJX-TEX" aria-hidden="true">
                            <mjx-mi class="mjx-i">
                                <mjx-c class="mjx-c1D441 TEX-I"></mjx-c>
                            </mjx-mi>
                            <mjx-mo class="mjx-n" space="3">
                                <mjx-c class="mjx-cD7"></mjx-c>
                            </mjx-mo>
                            <mjx-mi class="mjx-i" space="3">
                                <mjx-c class="mjx-c1D440 TEX-I"></mjx-c>
                            </mjx-mi>
                        </mjx-math>
						<span aria-hidden="true" class="no-mathjax mjx-copytext">$N \times M$</span>
                    </mjx-container> 크기의 직사각형으로 나타낼 수 있으며, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                        <mjx-math class="MJX-TEX" aria-hidden="true">
                            <mjx-mn class="mjx-n">
                                <mjx-c class="mjx-c31"></mjx-c>
                            </mjx-mn>
                            <mjx-mo class="mjx-n" space="3">
                                <mjx-c class="mjx-cD7"></mjx-c>
                            </mjx-mo>
                            <mjx-mn class="mjx-n" space="3">
                                <mjx-c class="mjx-c31"></mjx-c>
                            </mjx-mn>
                        </mjx-math>
						<span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \times 1$</span>
                    </mjx-container> 크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 벽 또는 빈 칸이다. 청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북 중 하나이다. 방의 각 칸은 좌표 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                        <mjx-math class="MJX-TEX" aria-hidden="true">
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c28"></mjx-c>
                            </mjx-mo>
                            <mjx-mi class="mjx-i">
                                <mjx-c class="mjx-c1D45F TEX-I"></mjx-c>
                            </mjx-mi>
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c2C"></mjx-c>
                            </mjx-mo>
                            <mjx-mi class="mjx-i" space="2">
                                <mjx-c class="mjx-c1D450 TEX-I"></mjx-c>
                            </mjx-mi>
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c29"></mjx-c>
                            </mjx-mo>
                        </mjx-math>
                        <span aria-hidden="true" class="no-mathjax mjx-copytext">$(r, c)$</span>
                    </mjx-container>로 나타낼 수 있고, 가장 북쪽 줄의 가장 서쪽 칸의 좌표가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                        <mjx-math class="MJX-TEX" aria-hidden="true">
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c28"></mjx-c>
                            </mjx-mo>
                            <mjx-mn class="mjx-n">
                                <mjx-c class="mjx-c30"></mjx-c>
                            </mjx-mn>
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c2C"></mjx-c>
                            </mjx-mo>
                            <mjx-mn class="mjx-n" space="2">
                                <mjx-c class="mjx-c30"></mjx-c>
                            </mjx-mn>
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c29"></mjx-c>
                            </mjx-mo>
                        </mjx-math>
                        <span aria-hidden="true" class="no-mathjax mjx-copytext">$(0, 0)$</span>
                    </mjx-container>, 가장 남쪽 줄의 가장 동쪽 칸의 좌표가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                        <mjx-math class="MJX-TEX" aria-hidden="true">
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c28"></mjx-c>
                            </mjx-mo>
                            <mjx-mi class="mjx-i">
                                <mjx-c class="mjx-c1D441 TEX-I"></mjx-c>
                            </mjx-mi>
                            <mjx-mo class="mjx-n" space="3">
                                <mjx-c class="mjx-c2212"></mjx-c>
                            </mjx-mo>
                            <mjx-mn class="mjx-n" space="3">
                                <mjx-c class="mjx-c31"></mjx-c>
                            </mjx-mn>
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c2C"></mjx-c>
                            </mjx-mo>
                            <mjx-mi class="mjx-i" space="2">
                                <mjx-c class="mjx-c1D440 TEX-I"></mjx-c>
                            </mjx-mi>
                            <mjx-mo class="mjx-n" space="3">
                                <mjx-c class="mjx-c2212"></mjx-c>
                            </mjx-mo>
                            <mjx-mn class="mjx-n" space="3">
                                <mjx-c class="mjx-c31"></mjx-c>
                            </mjx-mn>
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c29"></mjx-c>
                            </mjx-mo>
                        </mjx-math>
                        <span aria-hidden="true" class="no-mathjax mjx-copytext">$(N-1, M-1)$</span>
                    </mjx-container>이다. 즉, 좌표 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                        <mjx-math class="MJX-TEX" aria-hidden="true">
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c28"></mjx-c>
                            </mjx-mo>
                            <mjx-mi class="mjx-i">
                                <mjx-c class="mjx-c1D45F TEX-I"></mjx-c>
                            </mjx-mi>
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c2C"></mjx-c>
                            </mjx-mo>
                            <mjx-mi class="mjx-i" space="2">
                                <mjx-c class="mjx-c1D450 TEX-I"></mjx-c>
                            </mjx-mi>
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c29"></mjx-c>
                            </mjx-mo>
                        </mjx-math>
                        <span aria-hidden="true" class="no-mathjax mjx-copytext">$(r, c)$</span>
                    </mjx-container>는 북쪽에서 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                        <mjx-math class="MJX-TEX" aria-hidden="true">
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c28"></mjx-c>
                            </mjx-mo>
                            <mjx-mi class="mjx-i">
                                <mjx-c class="mjx-c1D45F TEX-I"></mjx-c>
                            </mjx-mi>
                            <mjx-mo class="mjx-n" space="3">
                                <mjx-c class="mjx-c2B"></mjx-c>
                            </mjx-mo>
                            <mjx-mn class="mjx-n" space="3">
                                <mjx-c class="mjx-c31"></mjx-c>
                            </mjx-mn>
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c29"></mjx-c>
                            </mjx-mo>
                        </mjx-math>
						<span aria-hidden="true" class="no-mathjax mjx-copytext">$(r+1)$</span>
                    </mjx-container>번째에 있는 줄의 서쪽에서 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                        <mjx-math class="MJX-TEX" aria-hidden="true">
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c28"></mjx-c>
                            </mjx-mo>
                            <mjx-mi class="mjx-i">
                                <mjx-c class="mjx-c1D450 TEX-I"></mjx-c>
                            </mjx-mi>
                            <mjx-mo class="mjx-n" space="3">
                                <mjx-c class="mjx-c2B"></mjx-c>
                            </mjx-mo>
                            <mjx-mn class="mjx-n" space="3">
                                <mjx-c class="mjx-c31"></mjx-c>
                            </mjx-mn>
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c29"></mjx-c>
                            </mjx-mo>
                        </mjx-math>
						<span aria-hidden="true" class="no-mathjax mjx-copytext">$(c+1)$</span>
                    </mjx-container>번째 칸을 가리킨다. 처음에 빈 칸은 전부 청소되지 않은 상태이다.</p>
                <p>로봇 청소기는 다음과 같이 작동한다.</p>
                <ol>
                    <li>현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.</li>
                    <li>현재 칸의 주변 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                            <mjx-math class="MJX-TEX" aria-hidden="true">
                                <mjx-mn class="mjx-n">
                                    <mjx-c class="mjx-c34"></mjx-c>
                                </mjx-mn>
                            </mjx-math>
                            <span aria-hidden="true" class="no-mathjax mjx-copytext">$4$</span>
                        </mjx-container>칸 중 청소되지 않은 빈 칸이 없는 경우,
                        <ol>
                            <li>바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.</li>
                            <li>바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.</li>
                        </ol>
                    </li>
                    <li>현재 칸의 주변 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                            <mjx-math class="MJX-TEX" aria-hidden="true">
                                <mjx-mn class="mjx-n">
                                    <mjx-c class="mjx-c34"></mjx-c>
                                </mjx-mn>
                            </mjx-math>
                            <span aria-hidden="true" class="no-mathjax mjx-copytext">$4$</span>
                        </mjx-container>칸 중 청소되지 않은 빈 칸이 있는 경우,
                        <ol>
                            <li>반시계 방향으로 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                                    <mjx-math class="MJX-TEX" aria-hidden="true">
                                        <mjx-msup>
                                            <mjx-mn class="mjx-n">
                                                <mjx-c class="mjx-c39"></mjx-c>
                                                <mjx-c class="mjx-c30"></mjx-c>
                                            </mjx-mn>
                                            <mjx-script style="vertical-align: 0.393em;">
                                                <mjx-mo class="mjx-n" size="s">
                                                    <mjx-c class="mjx-c2218"></mjx-c>
                                                </mjx-mo>
                                            </mjx-script>
                                        </mjx-msup>
                                    </mjx-math>
									<span aria-hidden="true" class="no-mathjax mjx-copytext">$90^\circ$</span>
                                </mjx-container> 회전한다.</li>
                            <li>바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.</li>
                            <li>1번으로 돌아간다.</li>
                        </ol>
                    </li>
                </ol>
            </div>
        </section>
    </div>
    <div class="col-md-12">
        <section id="input" class="problem-section">
            <div class="headline">
                <h2>입력</h2>
            </div>
            <div id="problem_input" class="problem-text">
                <p>첫째 줄에 방의 크기 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                        <mjx-math class="MJX-TEX" aria-hidden="true">
                            <mjx-mi class="mjx-i">
                                <mjx-c class="mjx-c1D441 TEX-I"></mjx-c>
                            </mjx-mi>
                        </mjx-math>
                        <span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span>
                    </mjx-container>과 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                        <mjx-math class="MJX-TEX" aria-hidden="true">
                            <mjx-mi class="mjx-i">
                                <mjx-c class="mjx-c1D440 TEX-I"></mjx-c>
                            </mjx-mi>
                        </mjx-math>
                        <span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span>
                    </mjx-container>이 입력된다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                        <mjx-math class="MJX-TEX" aria-hidden="true">
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c28"></mjx-c>
                            </mjx-mo>
                            <mjx-mn class="mjx-n">
                                <mjx-c class="mjx-c33"></mjx-c>
                            </mjx-mn>
                            <mjx-mo class="mjx-n" space="4">
                                <mjx-c class="mjx-c2264"></mjx-c>
                            </mjx-mo>
                            <mjx-mi class="mjx-i" space="4">
                                <mjx-c class="mjx-c1D441 TEX-I"></mjx-c>
                            </mjx-mi>
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c2C"></mjx-c>
                            </mjx-mo>
                            <mjx-mi class="mjx-i" space="2">
                                <mjx-c class="mjx-c1D440 TEX-I"></mjx-c>
                            </mjx-mi>
                            <mjx-mo class="mjx-n" space="4">
                                <mjx-c class="mjx-c2264"></mjx-c>
                            </mjx-mo>
                            <mjx-mn class="mjx-n" space="4">
                                <mjx-c class="mjx-c35"></mjx-c>
                                <mjx-c class="mjx-c30"></mjx-c>
                            </mjx-mn>
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c29"></mjx-c>
                            </mjx-mo>
                        </mjx-math>
                        <span aria-hidden="true" class="no-mathjax mjx-copytext">$(3 \le N, M \le 50)$</span>
                    </mjx-container>  둘째 줄에 처음에 로봇 청소기가 있는 칸의 좌표 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                        <mjx-math class="MJX-TEX" aria-hidden="true">
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c28"></mjx-c>
                            </mjx-mo>
                            <mjx-mi class="mjx-i">
                                <mjx-c class="mjx-c1D45F TEX-I"></mjx-c>
                            </mjx-mi>
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c2C"></mjx-c>
                            </mjx-mo>
                            <mjx-mi class="mjx-i" space="2">
                                <mjx-c class="mjx-c1D450 TEX-I"></mjx-c>
                            </mjx-mi>
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c29"></mjx-c>
                            </mjx-mo>
                        </mjx-math>
                        <span aria-hidden="true" class="no-mathjax mjx-copytext">$(r, c)$</span>
                    </mjx-container>와 처음에 로봇 청소기가 바라보는 방향 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                        <mjx-math class="MJX-TEX" aria-hidden="true">
                            <mjx-mi class="mjx-i">
                                <mjx-c class="mjx-c1D451 TEX-I"></mjx-c>
                            </mjx-mi>
                        </mjx-math>
                        <span aria-hidden="true" class="no-mathjax mjx-copytext">$d$</span>
                    </mjx-container>가 입력된다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                        <mjx-math class="MJX-TEX" aria-hidden="true">
                            <mjx-mi class="mjx-i">
                                <mjx-c class="mjx-c1D451 TEX-I"></mjx-c>
                            </mjx-mi>
                        </mjx-math>
                        <span aria-hidden="true" class="no-mathjax mjx-copytext">$d$</span>
                    </mjx-container>가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                        <mjx-math class="MJX-TEX" aria-hidden="true">
                            <mjx-mn class="mjx-n">
                                <mjx-c class="mjx-c30"></mjx-c>
                            </mjx-mn>
                        </mjx-math>
                        <span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span>
                    </mjx-container>인 경우 북쪽, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                        <mjx-math class="MJX-TEX" aria-hidden="true">
                            <mjx-mn class="mjx-n">
                                <mjx-c class="mjx-c31"></mjx-c>
                            </mjx-mn>
                        </mjx-math>
                        <span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span>
                    </mjx-container>인 경우 동쪽, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                        <mjx-math class="MJX-TEX" aria-hidden="true">
                            <mjx-mn class="mjx-n">
                                <mjx-c class="mjx-c32"></mjx-c>
                            </mjx-mn>
                        </mjx-math>
                        <span aria-hidden="true" class="no-mathjax mjx-copytext">$2$</span>
                    </mjx-container>인 경우 남쪽, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                        <mjx-math class="MJX-TEX" aria-hidden="true">
                            <mjx-mn class="mjx-n">
                                <mjx-c class="mjx-c33"></mjx-c>
                            </mjx-mn>
                        </mjx-math>
                        <span aria-hidden="true" class="no-mathjax mjx-copytext">$3$</span>
                    </mjx-container>인 경우 서쪽을 바라보고 있는 것이다.</p>
                <p>셋째 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                        <mjx-math class="MJX-TEX" aria-hidden="true">
                            <mjx-mi class="mjx-i">
                                <mjx-c class="mjx-c1D441 TEX-I"></mjx-c>
                            </mjx-mi>
                        </mjx-math>
                        <span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span>
                    </mjx-container>개의 줄에 각 장소의 상태를 나타내는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                        <mjx-math class="MJX-TEX" aria-hidden="true">
                            <mjx-mi class="mjx-i">
                                <mjx-c class="mjx-c1D441 TEX-I"></mjx-c>
                            </mjx-mi>
                            <mjx-mo class="mjx-n" space="3">
                                <mjx-c class="mjx-cD7"></mjx-c>
                            </mjx-mo>
                            <mjx-mi class="mjx-i" space="3">
                                <mjx-c class="mjx-c1D440 TEX-I"></mjx-c>
                            </mjx-mi>
                        </mjx-math>
                        <span aria-hidden="true" class="no-mathjax mjx-copytext">$N \times M$</span>
                    </mjx-container>개의 값이 한 줄에 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                        <mjx-math class="MJX-TEX" aria-hidden="true">
                            <mjx-mi class="mjx-i">
                                <mjx-c class="mjx-c1D440 TEX-I"></mjx-c>
                            </mjx-mi>
                        </mjx-math>
                        <span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span>
                    </mjx-container>개씩 입력된다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                        <mjx-math class="MJX-TEX" aria-hidden="true">
                            <mjx-mi class="mjx-i">
                                <mjx-c class="mjx-c1D456 TEX-I"></mjx-c>
                            </mjx-mi>
                        </mjx-math>
                        <span aria-hidden="true" class="no-mathjax mjx-copytext">$i$</span>
                    </mjx-container>번째 줄의 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                        <mjx-math class="MJX-TEX" aria-hidden="true">
                            <mjx-mi class="mjx-i">
                                <mjx-c class="mjx-c1D457 TEX-I"></mjx-c>
                            </mjx-mi>
                        </mjx-math>
                        <span aria-hidden="true" class="no-mathjax mjx-copytext">$j$</span>
                    </mjx-container>번째 값은 칸 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                        <mjx-math class="MJX-TEX" aria-hidden="true">
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c28"></mjx-c>
                            </mjx-mo>
                            <mjx-mi class="mjx-i">
                                <mjx-c class="mjx-c1D456 TEX-I"></mjx-c>
                            </mjx-mi>
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c2C"></mjx-c>
                            </mjx-mo>
                            <mjx-mi class="mjx-i" space="2">
                                <mjx-c class="mjx-c1D457 TEX-I"></mjx-c>
                            </mjx-mi>
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c29"></mjx-c>
                            </mjx-mo>
                        </mjx-math>
                        <span aria-hidden="true" class="no-mathjax mjx-copytext">$(i, j)$</span>
                    </mjx-container>의 상태를 나타내며, 이 값이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                        <mjx-math class="MJX-TEX" aria-hidden="true">
                            <mjx-mn class="mjx-n">
                                <mjx-c class="mjx-c30"></mjx-c>
                            </mjx-mn>
                        </mjx-math>
                        <span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span>
                    </mjx-container>인 경우 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                        <mjx-math class="MJX-TEX" aria-hidden="true">
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c28"></mjx-c>
                            </mjx-mo>
                            <mjx-mi class="mjx-i">
                                <mjx-c class="mjx-c1D456 TEX-I"></mjx-c>
                            </mjx-mi>
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c2C"></mjx-c>
                            </mjx-mo>
                            <mjx-mi class="mjx-i" space="2">
                                <mjx-c class="mjx-c1D457 TEX-I"></mjx-c>
                            </mjx-mi>
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c29"></mjx-c>
                            </mjx-mo>
                        </mjx-math>
                        <span aria-hidden="true" class="no-mathjax mjx-copytext">$(i, j)$</span>
                    </mjx-container>가 청소되지 않은 빈 칸이고, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                        <mjx-math class="MJX-TEX" aria-hidden="true">
                            <mjx-mn class="mjx-n">
                                <mjx-c class="mjx-c31"></mjx-c>
                            </mjx-mn>
                        </mjx-math>
                        <span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span>
                    </mjx-container>인 경우 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;">
                        <mjx-math class="MJX-TEX" aria-hidden="true">
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c28"></mjx-c>
                            </mjx-mo>
                            <mjx-mi class="mjx-i">
                                <mjx-c class="mjx-c1D456 TEX-I"></mjx-c>
                            </mjx-mi>
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c2C"></mjx-c>
                            </mjx-mo>
                            <mjx-mi class="mjx-i" space="2">
                                <mjx-c class="mjx-c1D457 TEX-I"></mjx-c>
                            </mjx-mi>
                            <mjx-mo class="mjx-n">
                                <mjx-c class="mjx-c29"></mjx-c>
                            </mjx-mo>
                        </mjx-math>
                        <span aria-hidden="true" class="no-mathjax mjx-copytext">$(i, j)$</span>
                    </mjx-container>에 벽이 있는 것이다. 방의 가장 북쪽, 가장 남쪽, 가장 서쪽, 가장 동쪽 줄 중 하나 이상에 위치한 모든 칸에는 벽이 있다. 로봇 청소기가 있는 칸은 항상 빈 칸이다.</p>
            </div>
        </section>
    </div>
    <div class="col-md-12">
        <section id="output" class="problem-section">
            <div class="headline">
                <h2>출력</h2>
            </div>
            <div id="problem_output" class="problem-text">
                <p>로봇 청소기가 작동을 시작한 후 작동을 멈출 때까지 청소하는 칸의 개수를 출력한다.</p>
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
                    <pre class="sampledata" id="sample-input-1">3 3
1 1 0
1 1 1
1 0 1
1 1 1
</pre>
                </section>
            </div>
            <div class="col-md-6">
                <section id="sampleoutput1">
                    <div class="headline">
                        <h2>예제 출력 1</h2>
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
                        <h2>예제 입력 2</h2>
                    </div>
                    <pre class="sampledata" id="sample-input-2">11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
</pre>
                </section>
            </div>
            <div class="col-md-6">
                <section id="sampleoutput2">
                    <div class="headline">
                        <h2>예제 출력 2</h2>
                    </div>
                    <pre class="sampledata" id="sample-output-2">57
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