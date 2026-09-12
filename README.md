# 🛍️ NexaRetail Sales Analytics Pipeline

> An automated ETL pipeline that cleans, validates, and loads NexaRetail's sales data into SQL Server — powering a 3-year (2023–2025) business intelligence review across revenue, profitability, and customer retention.
>
> 
> > A data-driven analysis across **Sales & Profitability**, **Product Performance**, and **Customer & Order Behavior** — uncovering the real story behind NexaRetail's revenue swings.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Cleaning-150458?logo=pandas&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM%20%2F%20Engine-D71F00?logo=python&logoColor=white)
![SQL Server](https://img.shields.io/badge/SQL%20Server-Data%20Warehouse-CC2927?logo=microsoftsqlserver&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Cross--platform-0078D6?logo=windows&logoColor=white)


---

## 🧭 Table of Contents

- [Executive Summary](#-executive-summary)
- [KPIs at a Glance](#-kpis-at-a-glance)
- [Dashboard 1 — Overview: Sales, Profit & Margin](#-dashboard-1--overview-sales-profit--margin)
- [Dashboard 2 — Product & Profitability Analysis](#-dashboard-2--product--profitability-analysis)
- [Dashboard 3 — Customer & Order Analysis](#-dashboard-3--customer--order-analysis)
- [Bringing It Together: Prioritized Action List](#-bringing-it-together-prioritized-action-list)
- [Key Takeaways](#-key-takeaways)

---

## 📌 Executive Summary

All three dashboards tell one consistent story: **2024 was a soft year, and 2025 was a recovery — but a narrower and more fragile one than the headline numbers suggest.**

Sales and profit dipped in 2024 and rebounded in 2025, but the 2025 rebound came from **fewer, higher-value orders** and a **shrinking, more concentrated customer base** — not broader demand. Beneath this up-and-down cycle, two problems have been quietly getting worse every year, regardless of the headline swings: **customer retention** and **loss-making orders in the Paper subcategory.**

### Highlights

| Insight | Detail |
|---|---|
| 🚀 **Technology is the core engine** | Drives the most sales and the sharpest swings; sits in the top profit-margin tier all three years. Its 2024 dip explains most of that year's company-wide decline. |
| 🏠 **Home Office overtook Consumer** | Became the top segment starting in 2024 and has stayed there — confirmed independently in both the Overview and Customer dashboards. |
| 📉 **Repeat customer rate fell 3 years straight** | 60.78% → 59.00% → 58.70% — the *only* metric in the entire review that moved in one direction the whole time. |
| 📄 **Paper's losses rose 60% in 3 years** | 15 → 18 → 24 loss-making orders, consistently the worst or near-worst offender. |
| ⚠️ **2025's recovery is real but narrow** | Sales, profit, and margin are all up — but customer count and order count are both *down*. Growth came from value per transaction, not more transactions or more customers. |

---

## 📈 KPIs at a Glance

| Metric | 2023 | 2024 | 2025 |
|---|---|---|---|
| **Total Sales** | Rs. 240.13M | Rs. 235.07M | Rs. 238.04M |
| **Total Profit** | Rs. 35.76M | Rs. 33.58M | Rs. 35.48M |
| **Profit Margin** | 14.89% | 14.28% | 14.90% |
| **Loss-Making Orders** | 191 | 209 | 200 |
| **Total Customers** | 1,614 | 1,627 | 1,603 |
| **Repeat Customers %** | 60.78% | 59.00% | 58.70% |

---

## 🗂️ Dashboard 1 — Overview: Sales, Profit & Margin

**Theme:** *The company-wide V-shape and what drove it.*

### What Happened

- **2023 → 2024 (Step Down):** Sales fell **2.11%** (Rs. 240.13M → Rs. 235.07M) and profit fell a sharper **6.09%** (Rs. 35.76M → Rs. 33.58M), pulling margin from 14.89% down to 14.28% — *even as order count rose 1.62%*. More orders, less revenue, and less profit together point to a shrinking basket size and margin pressure, not weaker demand.
- **2024 → 2025 (Recovery):** Sales rebounded to Rs. 238.04M (**+1.26%**) and profit jumped **5.66%** to Rs. 35.48M — a 3-year-high margin of **14.90%** — but with **fewer orders (-3.34%)**. The rebound was driven by fewer, richer orders, not more transactions.

### Why It Happened

- **Technology carried, then rescued, the business.** Sales dropped from Rs. 148.97M (2023) to Rs. 140.79M (2024) — the single biggest driver of that year's decline — before rebounding to Rs. 149.52M in 2025. Profit followed the identical V-shape (Rs. 24.7M → Rs. 22.4M → Rs. 24.6M).
- **Furniture moved opposite to Technology**, cushioning the 2024 dip (Rs. 77.4M → Rs. 80.63M) before falling back in 2025 (→ Rs. 74.53M).
- **Office Supplies stayed flat and small** (~Rs. 13.7–14M) throughout all three years.
- **The segment mix flipped and never fully reverted.** Consumer led in 2023 (Rs. 85M); Home Office overtook it in 2024 (Rs. 82M vs. Rs. 75M) and extended its lead in 2025 (Rs. 84M vs. Rs. 76M) — a durable shift in NexaRetail's buyer base, independently confirmed by the Customer & Order dashboard.

### What To Do

1. **Protect Technology, but reduce dependence on it.** It swings the whole P&L — build a second engine, with Furniture's 2024 performance showing it can carry growth when incentivized.
2. **Double down on segments gaining share.** Home Office's two-year lead deserves proportionally more marketing and inventory investment.
3. **Track margin, not just sales, as the headline KPI.** 2024 shows that sales alone would have hidden a much worse profit story.

---

## 🧮 Dashboard 2 — Product & Profitability Analysis

**Theme:** *Where losses hide, and why discounting is dangerous.*

### What Happened

- **Loss-making orders followed their own mini-cycle:** 191 (2023) → 209 (2024, **+9.42%**, tracking that year's margin squeeze) → 200 (2025, **-4.31%**, part of the recovery, but still ~5% above 2023). Even with the headline recovery, the business generates more bad orders than it did in 2023.
- **Paper stands out for the wrong reason** — its loss-making orders climbed every single year: **15 → 18 → 24 (a 60% increase)**, becoming the single largest source of loss-making orders in both 2024 and 2025.
- **Sofas stayed chronically high** (15 → 17 → 16).
- **Tables improved sharply** (14 → 11 → 7) — proof that the pattern is fixable.

### Why It Happened

- In every year, the **0% discount band generates the overwhelming majority of profit** (~Rs. 17M), with profit collapsing sharply as soon as *any* discount is applied — a pattern that holds identically across all three years.
- **Paper is structurally fragile:** it's low-ticket, so shipping/handling cost is a much larger share of order value than for Technology items. Any discount or cost increase pushes a slice of Paper orders below breakeven — and the steady multi-year climb suggests worsening underlying economics, not a one-off blip.
- The same logic applies to **Sofas, Tables, and Pens** — thin base margins make them disproportionately likely to turn into losses once discounted.
- **Technology's healthier 15–17% margin** gives it far more room to absorb a discount before turning unprofitable — which is exactly why it stays out of the loss-order conversation entirely.

### What To Do

1. **Investigate Paper specifically, now.** A 60% rise in loss-making orders over three straight years is the clearest deteriorating trend in the dataset. Check discounting, shipping cost per order, or a specific vendor/channel, and fix pricing or set a minimum order value.
2. **Cap or eliminate discounting on structurally thin-margin subcategories.** Paper, Pens, Sofas, and Tables are the categories most likely to flip into a loss once discounted.
3. **Study what fixed Tables — and replicate it.** Its loss-order count fell every year, while Paper and Sofas didn't. This is an internal case study, not a hypothesis.
4. **Keep prioritizing Technology.** Laptops, printers, accessories, monitors, and phones compound on two fronts at once — revenue and margin.

---

## 👥 Dashboard 3 — Customer & Order Analysis

**Theme:** *Retention is quietly eroding beneath a stable customer count.*

### What Happened

- **Customer count barely moved:** 1,614 → 1,627 (**+0.81%**) → 1,603 (**-1.48%**) — ending slightly below where it started.
- **Average Order Value (AOV) told a different story:** it dropped to a low of Rs. 72.00K in 2024 (**-3.67%**), then jumped to a three-year high of **Rs. 75.42K in 2025 (+4.76%)** — even as customer count fell. 2025's revenue held up because remaining customers spent *more per order*, not because there were more customers.
- **Repeat customer rate is the one metric that never stopped sliding:** **60.78% → 59.00% → 58.70%**, down every single year. Everything else in this review moved in a V-shape; retention moved in one direction only.

### Why It Happened

- **The top 5 customers by sales are completely different people every year** — no customer ID repeats across 2023, 2024, and 2025.
- The top customer's spend grew sharply, from **Rs. 0.94M (2023) → Rs. 1.24M (2024) → Rs. 1.10M (2025)**. New customers keep arriving, but they aren't sticking — NexaRetail is **replacing** its best customers each year rather than **deepening relationships** with them.
- **2024's AOV dip lines up with that year's shrinking basket size** and margin compression from Dashboard 1 — the customer-level cause of 2024's revenue softness.
- **2025's higher AOV with fewer customers** confirms the "fewer, richer orders" pattern — but it also means revenue leans more heavily on a shrinking, higher-spending core.
- **Shipping behavior shifted too:** Standard Class orders declined every year (1,240 → 1,180 → 1,121), while Second Class rose every year (384 → 407 → 449) — consistent with the Home Office segment's less time-sensitive, more price-sensitive buying pattern.

### What To Do

1. **Treat the repeat-rate decline as the top-priority metric to fix.** It's the only trend that worsened three years straight — build a loyalty or win-back program aimed specifically at reversing it.
2. **Build a retention track for top spenders.** Since the highest-value customers are different people every year, create an account-management program that identifies each year's top spenders early and works to keep them.
3. **Don't mistake 2025's AOV strength for solved growth.** It's coming from a shrinking, higher-spending base — pair any upsell push with the retention fix above.
4. **Lean into the Standard-to-Second-Class shift.** If it reflects genuine Home Office buyer preference, consider tiered shipping incentives that match this behavior without giving away unnecessary margin.

---

## 🎯 Bringing It Together: Prioritized Action List

Read together, the three dashboards point to the same underlying business: **strong on Technology, increasingly reliant on Home Office, and a shrinking pool of high-value customers** — all while quietly leaking value through repeat-customer attrition and a handful of structurally unprofitable subcategories.

| Priority | Action | Why It Matters |
|---|---|---|
| **1** | **Fix retention before chasing more growth** | Repeat customer rate is the only metric that fell three years running. Until this reverses, every year's hard-won customers are simply being replaced, not retained — capping the compounding value of any other improvement. |
| **2** | **Resolve Paper's losses & cap discounting on thin-margin subcategories** | Paper, Sofas, Tables, and Pens are simultaneously the categories with the most loss-making orders and the ones most sensitive to discounting. A controllable, near-term fix. |
| **3** | **Protect and grow Technology while building a second engine** | Technology drives sales, profit, and margin simultaneously — but the business's exposure to a single category is a structural risk worth diversifying, with Furniture the most promising candidate. |
| **4** | **Design specifically around the Home Office buyer** | This segment now leads sales, favors slower/cheaper shipping, and shows up consistently across both the Overview and Customer dashboards — it should be the primary segment for merchandising and fulfillment decisions. |
| **5** | **Manage customer concentration risk** | Top-customer spend has risen ~20–30% since 2023 even as total customers shrank slightly; a small base of large accounts now carries more weight, and losing one matters more than it used to. |

---

## 🔑 Key Takeaways

- 📊 **The headline numbers hide a fragile recovery** — 2025 looks strong on the surface, but growth came from fewer, higher-value transactions, not a healthier, broader business.
- 🔻 **Retention is the single biggest long-term threat** — it's the only metric that has consistently worsened, regardless of the yearly ups and downs elsewhere.
- 💸 **Discounting is dangerous on thin-margin products** — Paper, Sofas, Tables, and Pens all show that even small discounts can flip an order into a loss.
- 🖥️ **Technology remains the backbone** — but overreliance on a single category is a structural risk worth actively diversifying against.
- 🏠 **Home Office is the segment of the future** — it has led sales for two consecutive years and deserves to be treated as the primary customer segment going forward.

---

<p align="center"><i>Report period: 2023–2025 · Source: NexaRetail Three-Year Review (Overview, Product & Profitability, and Customer & Order dashboards)</i></p>
