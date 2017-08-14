from flask import render_template, redirect, url_for, flash
from app import app
import itertools
import string

cmdrs = {'R':[], 'G':[], 'U':['Baral, Chief of Compliance'],'W':[],'R':[], 'WU' : []}

def find_color(clr):
	global cmdrs
	found = False
	key = ''
	for combo in cmdrs.keys():
		if clr in [''.join(i) for i in itertools.product(combo, repeat=len(combo))]:
			found = True
			key = combo
	return found, key

@app.route('/')
@app.route('/home')
def home():
	global cmdrs
	return render_template('home.html', colors = cmdrs.keys())

@app.route('/<color>')
def color_page(color):
	global cmdrs
	color = color.upper()
	found, key = find_color(color)
	if not found:
		return redirect(url_for('home'))
	else:
		#[{} for i in cmdrs[key]]
		x = {}
		for cmdr in cmdrs[key]:
			x[cmdr] = cmdr.translate(None, string.punctuation).replace(' ', '-').lower()
		#cmdr_links = [cmdr.translate(None, string.punctuation).replace(' ', '-').lower() for cmdr in cmdrs[key]]
		return render_template('color_page.html', colors=cmdrs.keys(), color=key,  commanders = x)

@app.route('/<color>/<cmdr>')
def commander(color, cmdr):
	global cmdrs
	color = color.upper()
	found, key = find_color(color)
	if not found:
		flash('Color not found')
		return redirect(url_for('home'))
	l_cmdr = cmdr.split('-')
	found = False
	for t_cmdr in cmdrs[key]:
		prop_cmdr = t_cmdr	
		t_cmdr = t_cmdr.lower()
		tst = t_cmdr.translate(None, string.punctuation)
		l_tst = tst.split()
		if l_cmdr == l_tst:
			found = True
			cmdr = prop_cmdr
	if not found:
		flash('Commander not found')
		return redirect(url_for('home'))
	return render_template('commander_page.html', colors = cmdrs.keys(), commander = cmdr)
