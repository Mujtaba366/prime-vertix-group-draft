const mobileMenu = document.getElementById('mobileMenu');
const menuToggle = document.getElementById('menuToggle');
const menuIcon = menuToggle ? menuToggle.querySelector('.menu-icon') : null;
const closeIcon = menuToggle ? menuToggle.querySelector('.close-icon') : null;
const enrolModalOverlay = document.getElementById('enrolModalOverlay');

function showEnrolModal(){
    if(!enrolModalOverlay) return;
    const form = document.getElementById('enrolForm');
    const dateInput = document.getElementById('signatureDate');
    if(form) form.reset();
    if(dateInput) dateInput.value = new Date().toISOString().slice(0,10);
    document.getElementById('enrolModalStep1')?.classList.remove('hidden');
    document.getElementById('enrolModalStep2')?.classList.add('hidden');
    enrolModalOverlay.classList.remove('hidden');
    enrolModalOverlay.classList.add('flex');
    document.body.style.overflow = 'hidden';
}

function hideEnrolModal(){
    if(!enrolModalOverlay) return;
    enrolModalOverlay.classList.add('hidden');
    enrolModalOverlay.classList.remove('flex');
    document.body.style.overflow = '';
}

function goEnrolStep(step){
    const step1 = document.getElementById('enrolModalStep1');
    const step2 = document.getElementById('enrolModalStep2');
    if(!step1 || !step2) return;
    if(step === 1){
        step1.classList.remove('hidden');
        step2.classList.add('hidden');
    } else {
        step1.classList.add('hidden');
        step2.classList.remove('hidden');
    }
}

function handleEnrolSubmit(event){
    event.preventDefault();
    const step2 = document.getElementById('enrolModalStep2');
    const step1 = document.getElementById('enrolModalStep1');
    if(step1?.classList.contains('hidden')){
        // Step 2: submit the form
        document.getElementById('enrolForm').submit();
    } else {
        // Step 1: go to step 2
        goEnrolStep(2);
    }
    return false;
}

if(enrolModalOverlay){
    enrolModalOverlay.addEventListener('click', (event) => {
        if(event.target === enrolModalOverlay) hideEnrolModal();
    });
}

document.addEventListener('keydown', (event) => {
if(event.key === 'Escape' && enrolModalOverlay && !enrolModalOverlay.classList.contains('hidden')){
    hideEnrolModal();
}
});
function toggleMenu(){
if(!mobileMenu) return;
    const isOpen = mobileMenu.classList.contains('opacity-100');
    if(isOpen){
        mobileMenu.classList.remove('max-h-96','opacity-100');
        mobileMenu.classList.add('max-h-0','opacity-0');
        if(menuIcon) menuIcon.classList.remove('hidden');
        if(closeIcon) closeIcon.classList.add('hidden');
    } else {
        mobileMenu.classList.remove('max-h-0','opacity-0');
        mobileMenu.classList.add('max-h-96','opacity-100');
        if(menuIcon) menuIcon.classList.add('hidden');
        if(closeIcon) closeIcon.classList.remove('hidden');
    }
}

function handleNav(href){
    try{
        const el = document.querySelector(href);
        if(el){
        el.scrollIntoView({behavior:'smooth', block:'start'});
        } else {
        window.location.href = href;
        }
    }catch(e){
        window.location.href = href;
    }
    if(mobileMenu && mobileMenu.classList.contains('opacity-100')) toggleMenu();
}
if (window.lucide) {
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => lucide.createIcons());
    } else {
        lucide.createIcons();
    }
}
function ensureLucideFallbacks(){
    const nodes = document.querySelectorAll('[data-lucide]');
    nodes.forEach(el => {
        if (el.querySelector('svg')) return; // already rendered
        const name = (el.getAttribute('data-lucide') || '').toLowerCase();
        let svg = '';
        switch(name){
        case 'target':
            svg = '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="6" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="2" fill="currentColor"/></svg>';
            break;
        case 'eye':
            svg = '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="2"/></svg>';
            break;
        case 'lightbulb':
            svg = '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M9 18h6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><path d="M10 22h4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><path d="M9 10a3 3 0 116 0c0 1.657-1 3-2 3v2H11v-2c-1 0-2-1.343-2-3z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
            break;
        case 'award':
            svg = '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><circle cx="12" cy="8" r="4" stroke="currentColor" stroke-width="2"/><path d="M8 21l4-3 4 3" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
            break;
        case 'brain':
            svg = '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M20 12c0-2.5-2-4.5-4.5-4.5-.3 0-.6 0-.9.1A3.5 3.5 0 0 0 11 6C9 6 7.5 7.5 7.5 9.5S9 13 11 13h7z" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M4 12c0 2.5 2 4.5 4.5 4.5.3 0 .6 0 .9-.1A3.5 3.5 0 0 0 13 18c2 0 3.5-1.5 3.5-3.5S15 11 13 11H4z" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>';
            break;
        case 'code-2':
            svg = '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M8 9l-4 3 4 3" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M16 9l4 3-4 3" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
            break;
        case 'book-open':
            svg = '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M2 7a2 2 0 0 1 2-2h7v14H4a2 2 0 0 1-2-2V7z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M22 7a2 2 0 0 0-2-2h-7v14h7a2 2 0 0 0 2-2V7z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
            break;
        case 'layers':
            svg = '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M12 2l9 6-9 6-9-6 9-6z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M3 14l9 6 9-6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
            break;
        case 'star':
            svg = '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>';
            break;
        case 'map-pin':
            svg = '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M21 10c0 7-9 12-9 12S3 17 3 10a9 9 0 1118 0z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="12" cy="10" r="3" stroke="currentColor" stroke-width="2"/></svg>';
            break;
        case 'clock':
            svg = '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/><path d="M12 6v6l4 2" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
            break;
        case 'calendar':
            svg = '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><rect x="3" y="4" width="18" height="18" rx="2" stroke="currentColor" stroke-width="2"/><path d="M16 2v4M8 2v4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
            break;
        case 'users':
            svg = '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M17 21v-2a4 4 0 00-4-4H9a4 4 0 00-4 4v2" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="12" cy="7" r="4" stroke="currentColor" stroke-width="2"/></svg>';
            break;
        case 'monitor':
            svg = '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><rect x="2" y="3" width="20" height="14" rx="2" stroke="currentColor" stroke-width="2"/><path d="M8 21h8" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
            break;
        case 'check-circle':
            svg = '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/><path d="M9 12l2 2 4-4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
            break;
        case 'send':
            svg = '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M22 2L11 13" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M22 2l-7 20  -4-9-9-4 20-7z" stroke="currentColor" stroke-width="0"/></svg>';
            break;
        case 'mail':
            svg = '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M3 8l9 6 9-6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M21 19H3a2 2 0 01-2-2V7a2 2 0 012-2h18a2 2 0 012 2v10a2 2 0 01-2 2z" stroke="currentColor" stroke-width="0"/></svg>';
            break;
        case 'sparkles':
            svg = '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M12 2l1.5 3.5L17 7l-3.5 1.5L12 12 10.5 8.5 7 7l3.5-1.5L12 2z" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M5 13l1 2 2 1-2 1-1 2-1-2-2-1 2-1 1-2z" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>';
            break;
        default:
            svg = '';
        }
        if(svg) el.innerHTML = svg;
    });
}
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => setTimeout(ensureLucideFallbacks, 30));
} else {
    setTimeout(ensureLucideFallbacks, 30);
}