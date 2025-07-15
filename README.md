# Coding-Test
Coding Test<br>
[DFS와 BFS](https://www.acmicpc.net/problem/1260)
<div class="row">
		<div class="col-md-12">
			<div id="result_log"></div>
		</div>
		<div class="col-md-12">
							<ul class="nav nav-pills no-print problem-menu"><li class="active">
		<a href="/problem/1260"><img src="https://d2gd6pc034wcta.cloudfront.net/tier/9.svg" class="solvedac-tier">&nbsp;1260번</a>
</li><li><a href="/submit/1260">제출</a></li><li><a href="/problem/status/1260">맞힌 사람</a></li><li><a href="/short/status/1260">숏코딩</a></li><li><a href="/problem/history/1260">재채점 결과</a></li><li><a href="/status?from_problem=1&amp;problem_id=1260">채점 현황</a></li><li><a href="/status?from_mine=1&amp;problem_id=1260&amp;user_id=kwon_ga">내 제출</a></li><li><a href="https://solved.ac/contribute/1260" target="_blank">난이도 기여 <i class="fa fa-external-link"></i></a></li><li class="dropdown"><a class="dropdown-toggle" id="drop5" role="button" data-toggle="dropdown" href="#">강의<b class="caret"></b></a><ul id="menu2" class="dropdown-menu" role="menu" aria-labelledby="drop5"><li><a tabindex="-1" href="https://code.plus/course/42">알고리즘 기초 2/2</a></li><li><a tabindex="-1" href="https://code.plus/course/51">코딩 테스트 준비 - 기초</a></li></ul></li><li><a href="/board/search/all/problem/1260">질문 게시판</a></li></ul>
					</div>
		<div class="col-md-12">
			<div class="page-header">
				<h1><span class="printable">
	1260번
 - </span><span id="problem_title">DFS와 BFS</span>
				<span class="problem-label problem-label-ac">성공</span>				<div class="btn-group pull-right problem-button">
																										<button class="btn btn-default" type="button" id="favorite_button" data-favorite="0"><span class="glyphicon glyphicon-star-empty" id="favorite_image"></span></button>
																																						</div>
				</h1>
									
							</div>
		</div>
		<div class="col-md-12"><div class="table-responsive"><table class="table" id="problem-info"><thead><tr><th style="width:16%;">시간 제한</th><th style="width:16%;">메모리 제한</th><th style="width:17%;">제출</th><th style="width:17%;">정답</th><th style="width:17%;">맞힌 사람</th><th style="width:17%;">정답 비율</th></tr></thead><tbody><tr><td>2 초 </td><td>128 MB</td><td>337029</td><td>135839</td><td>80173</td><td>38.831%</td></tr></tbody></table></div></div>
						<div id="problem-body" class="">
			<div class="col-md-12">
				<section id="description" class="problem-section">
				<div class="headline">
				<h2>문제</h2>
				</div>
				<div id="problem_description" class="problem-text">
				<p>그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.&nbsp;정점 번호는 1번부터 N번까지이다.</p>

				</div>
				</section>
			</div>
										<div class="col-md-12">
					<section id="input" class="problem-section">
					<div class="headline">
					<h2>입력</h2>
					</div>
					<div id="problem_input" class="problem-text">
					<p>첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.</p>

					</div>
					</section>
				</div>
	
				<div class="col-md-12">
					<section id="output" class="problem-section">
					<div class="headline">
					<h2>출력</h2>
					</div>
					<div id="problem_output" class="problem-text">
					<p>첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.</p>

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
							<button type="button" class="btn btn-link copy-button" style="padding: 0px;" data-clipboard-target="#sample-input-1">복사</button>
						</h2>
						</div>
						<pre class="sampledata" id="sample-input-1">4 5 1
1 2
1 3
1 4
2 4
3 4
</pre>
						</section>
					</div>
					<div class="col-md-6">
						<section id="sampleoutput1">
						<div class="headline">
						<h2>예제 출력 1
							<button type="button" class="btn btn-link copy-button" style="padding: 0px;" data-clipboard-target="#sample-output-1">복사</button>
						</h2>
						</div>
						<pre class="sampledata" id="sample-output-1">1 2 4 3
1 2 3 4
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
							<button type="button" class="btn btn-link copy-button" style="padding: 0px;" data-clipboard-target="#sample-input-2">복사</button>
						</h2>
						</div>
						<pre class="sampledata" id="sample-input-2">5 5 3
5 4
5 2
1 2
3 4
3 1
</pre>
						</section>
					</div>
					<div class="col-md-6">
						<section id="sampleoutput2">
						<div class="headline">
						<h2>예제 출력 2
							<button type="button" class="btn btn-link copy-button" style="padding: 0px;" data-clipboard-target="#sample-output-2">복사</button>
						</h2>
						</div>
						<pre class="sampledata" id="sample-output-2">3 1 2 5 4
3 1 4 2 5
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
							<button type="button" class="btn btn-link copy-button" style="padding: 0px;" data-clipboard-target="#sample-input-3">복사</button>
						</h2>
						</div>
						<pre class="sampledata" id="sample-input-3">1000 1 1000
999 1000
</pre>
						</section>
					</div>
					<div class="col-md-6">
						<section id="sampleoutput3">
						<div class="headline">
						<h2>예제 출력 3
							<button type="button" class="btn btn-link copy-button" style="padding: 0px;" data-clipboard-target="#sample-output-3">복사</button>
						</h2>
						</div>
						<pre class="sampledata" id="sample-output-3">1000 999
1000 999
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
									<div class="col-md-12"><section id="source"><div class="headline"><h2>출처</h2></div><ul><li>문제를 만든 사람:&nbsp;<a href="/user/author5">author5</a></li><li>데이터를 추가한 사람:&nbsp;<a href="/user/dfghcvb11">dfghcvb11</a>, <a href="/user/djm03178">djm03178</a>, <a href="/user/doju">doju</a></li><li>어색한 표현을 찾은 사람:&nbsp;<a href="/user/doju">doju</a></li><li>빠진 조건을 찾은 사람:&nbsp;<a href="/user/pumpyboom">pumpyboom</a></li></ul></section></div>
													<div class="col-md-12">
					<section id="problem_tags">
					<div class="headline">
					<h2>알고리즘 분류</h2>
					</div>
																																												  <ul class="spoiler-list">
  						  							<li>
  							<a href="/problem/tag/7" class="spoiler-link">그래프 이론</a>
  							</li>
  						  							<li>
  							<a href="/problem/tag/11" class="spoiler-link">그래프 탐색</a>
  							</li>
  						  							<li>
  							<a href="/problem/tag/126" class="spoiler-link">너비 우선 탐색</a>
  							</li>
  						  							<li>
  							<a href="/problem/tag/127" class="spoiler-link">깊이 우선 탐색</a>
  							</li>
  						  					</ul>
										</section>
				</div>
																						<div class="col-md-12">
					<section id="problem_memo">
					<div class="headline">
					<h2>메모</h2>
					</div>
						<div id="problem-memo-view" class="problem-text">
			</div>
	<div id="problem-memo-edit" style="display: none;"><textarea name="memo-content" id="memo-content" class="form-control" style="display:none;"></textarea><div class="editor-toolbar"><a title="Bold (Ctrl-B)" tabindex="-1" class="fa fa-bold"></a><a title="Italic (Ctrl-I)" tabindex="-1" class="fa fa-italic"></a><a title="Heading (Ctrl-H)" tabindex="-1" class="fa fa-header"></a><a title="Big Heading" tabindex="-1" class="fa fa-header fa-header-x fa-header-1"></a><a title="Medium Heading" tabindex="-1" class="fa fa-header fa-header-x fa-header-2"></a><a title="Small Heading" tabindex="-1" class="fa fa-header fa-header-x fa-header-3"></a><i class="separator">|</i><a title="Code (Ctrl-Alt-C)" tabindex="-1" class="fa fa-code"></a><a title="Quote (Ctrl-')" tabindex="-1" class="fa fa-quote-left"></a><a title="Generic List (Ctrl-L)" tabindex="-1" class="fa fa-list-ul"></a><a title="Numbered List (Ctrl-Alt-L)" tabindex="-1" class="fa fa-list-ol"></a><a title="Insert Horizontal Line" tabindex="-1" class="fa fa-minus"></a><i class="separator">|</i><a title="Create Link (Ctrl-K)" tabindex="-1" class="fa fa-link"></a><a title="Insert Image (Ctrl-Alt-I)" tabindex="-1" class="fa fa-picture-o"></a><i class="separator">|</i><a title="Toggle Preview (Ctrl-P)" tabindex="-1" class="fa fa-eye no-disable"></a><a title="Toggle Side by Side (F9)" tabindex="-1" class="fa fa-columns no-disable no-mobile"></a><a title="Toggle Fullscreen (F11)" tabindex="-1" class="fa fa-arrows-alt no-disable no-mobile"></a></div><div class="CodeMirror cm-s-paper CodeMirror-wrap"><div style="overflow: hidden; position: relative; width: 3px; height: 0px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" cm-not-content="true"><div style="min-width: 1px;"></div></div><div class="CodeMirror-hscrollbar" cm-not-content="true"><div style="height: 100%; min-height: 1px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px;"><div style="position: relative;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span>xxxxxxxxxx</span></pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors"></div><div class="CodeMirror-code"></div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px;"></div><div class="CodeMirror-gutters" style="display: none;"></div></div></div><div class="editor-preview-side"></div><div class="editor-statusbar"><span class="autosave"></span><span class="lines">1</span><span class="words">0</span><span class="cursor">0:0</span></div></div><p class="lead text-center no-print" id="problem-memo-button"><a href="#" class="problem-memo-write">메모 작성하기</a></p><p class="lead text-center no-print" id="problem-memo-save-div" style="display: none;"><button type="button" class="btn btn-primary btn-lg" id="problem-memo-save" data-loading-text="작성 중...">저장</button>&nbsp;<button type="button" class="btn btn-lg" id="problem-memo-cancel">취소</button></p>

					</section>
				</div>
						</div>
