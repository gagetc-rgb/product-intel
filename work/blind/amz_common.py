"""Amazon US search, top organic results: 'bought in past month' badges, review counts, price."""
import json, re, pathlib, urllib.parse
from playwright.sync_api import sync_playwright
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36"
JS = r"""()=>[...document.querySelectorAll('div[data-component-type="s-search-result"]')].slice(0,24).map(d=>{
  const t=d.innerText; const h=d.querySelector('h2');
  const r=d.querySelector('a[href*="customerReviews"] span, span.s-underline-text');
  const b=(t.match(/([\d,.]+K?\+?) bought in past month/)||[])[1]||'';
  const p=d.querySelector('.a-price .a-offscreen');
  return {title:(h?h.innerText:'').slice(0,90), rev:r?r.innerText:'', bought:b, sp:/\bSponsored\b/.test(t), price:p?p.textContent:''};})"""
def num(s):
    s = s.strip("()+ ").replace(",", "")
    if not s: return 0
    m = 1000 if s.endswith("K") else 1
    try: return int(float(s.rstrip("K")) * m)
    except ValueError: return 0
