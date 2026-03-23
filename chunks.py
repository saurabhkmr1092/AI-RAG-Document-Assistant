def create_chunks():
    chunks = []

    # DOCUMENT 1: OVERVIEW

    chunks.append({
        "id": "overview",
        "text": "Indecimal provides end-to-end home construction support with transparent pricing, quality assurance, and structured project tracking from inquiry to handover."
    })

    chunks.append({
        "id": "principles",
        "text": """Indecimal operating principles include smooth construction experience, competitive pricing with no hidden charges, quality assurance with 445+ checks, stage-based contractor payments after verified completion, and transparent agreements with real-time project tracking."""
    })

    chunks.append({
        "id": "differentiators",
        "text": """Indecimal differentiators include warranty and post-delivery support, 100% transparent pricing, fixed timelines with delay penalties, branded materials with quality checks, and real-time project tracking dashboard."""
    })

    # CUSTOMER JOURNEY
    
    journey_steps = [
        "Customer raises a request by sharing plot details and vision.",
        "Customer meets experts including architects and specialists.",
        "Indecimal assists with home financing process.",
        "Customer designs a custom home with architects.",
        "Customer receives detailed design and transparent cost plans.",
        "Customer books the project with milestone-based payments.",
        "Construction progress is tracked in real-time with live updates.",
        "Interior customization is provided if required.",
        "Customer moves in after project completion and handover.",
        "Maintenance support is provided post-handover."
    ]

    for i, step in enumerate(journey_steps):
        chunks.append({
            "id": f"journey_{i+1}",
            "text": step
        })

    
    # DOCUMENT 2: PRICING
    
    chunks.append({
        "id": "pricing_packages",
        "text": """Indecimal pricing per sqft: Essential ₹1851, Premier ₹1995, Infinia ₹2250, Pinnacle ₹2450, inclusive of GST."""
    })

    # MATERIALS (grouped smartly)
    chunks.append({
        "id": "materials",
        "text": """Construction materials include steel (Fe 550/550D), cement (43 and 53 grade), aggregates (20mm and 40mm), RCC mix (M20/M25), and standard ceiling height of 10 ft."""
    })

    # KITCHEN
    chunks.append({
        "id": "kitchen_wallet",
        "text": """Kitchen wallet includes ceramic wall dado (₹40–₹90/sqft), sink (₹4000–₹10000), and faucet (₹2000–₹4000) depending on package."""
    })

    # BATHROOM
    chunks.append({
        "id": "bathroom_wallet",
        "text": """Bathroom wallet includes ceramic dado (₹40–₹90/sqft), sanitary fittings (₹32000–₹80000 per 1000 sqft), and CPVC piping brands depending on package."""
    })

    # DOORS & WINDOWS
    chunks.append({
        "id": "doors_windows",
        "text": """Main door budget ranges ₹20000–₹50000 depending on package. Windows are UPVC/aluminium with ₹440–₹700 per sqft allowance."""
    })

    # PAINTING
    chunks.append({
        "id": "painting",
        "text": """Interior painting includes putty, primer, and emulsion coats. Exterior painting includes primer and emulsion with brand variations across packages."""
    })

    # FLOORING
    chunks.append({
        "id": "flooring",
        "text": """Flooring ranges from ₹50/sqft to ₹170/sqft depending on package and area such as living, dining, or rooms."""
    })

    # FAQ (wallet)
    chunks.append({
        "id": "wallet_explanation",
        "text": "Wallet amounts are spending caps; upgrades can be customized at additional cost with equivalent brand options."
    })

    
    # DOCUMENT 3: POLICIES
   
    chunks.append({
        "id": "escrow_payment",
        "text": """Payments are made to an escrow account and released only after project manager verifies stage completion."""
    })

    chunks.append({
        "id": "delay_management",
        "text": """Delay prevention uses project tracking, deviation alerts, automated task assignment, and penalties for accountability."""
    })

    chunks.append({
        "id": "quality_system",
        "text": """Indecimal uses 445+ checkpoints covering structural integrity, safety, and execution quality with dashboard visibility."""
    })

    chunks.append({
        "id": "maintenance_program",
        "text": """Zero-cost maintenance covers plumbing, electrical, masonry, kitchen, fittings, roofing, painting, and more after handover."""
    })

    chunks.append({
        "id": "financing_support",
        "text": """Financing support includes relationship manager, minimal documentation, ~7 day confirmation and ~30 day disbursal (terms apply)."""
    })

    chunks.append({
        "id": "team_structure",
        "text": """Team includes advisors, architects, project managers, engineers, interior team, and maintenance support."""
    })

    chunks.append({
        "id": "partner_onboarding",
        "text": """Partners undergo project verification, background checks, agreement signing, and onboarding for quality assurance."""
    })

    return chunks


if __name__ == "__main__":
    chunks = create_chunks()
    print(f"Total chunks: {len(chunks)}")
    for c in chunks[:5]:
        print(c["id"], "->", c["text"][:80])