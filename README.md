# Prime Vertix Group — Lessons Site (Flask)

Minimal Flask site scaffold for Prime Vertix Group. Features:

- Public pages: Home, Lessons, Register
- Stripe Checkout integration for payments
- Supabase integration point for storing registrations
- Tailwind (CDN) & Lucide icons

Setup

1. Copy `.env.example` to `.env` and fill keys:

```
SUPABASE_URL=your-supabase-url
SUPABASE_KEY=your-supabase-key
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLISHABLE_KEY=pk_test_...
SECRET_KEY=some-secret
```

2. Create a virtualenv and install requirements:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

3. Run the app:

```bash
python app.py
```

Notes

- Place your company `logo.png` and other assets listed in `static/IMAGE_LIST.txt` inside the `static/` folder.
- The shop page is intentionally not linked; create later when ready.
- To record registrations you must create a `registrations` table in Supabase with suitable columns (name,email,age,phone,course,status,checkout_session_id).

If you want, I can:

- Add a database migration SQL for Supabase
- Wire up a webhook to mark registrations as paid after Stripe confirmation
- Deploy to a platform (Render, Vercel serverless, Railway)
