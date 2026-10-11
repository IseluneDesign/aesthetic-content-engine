<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aesthetic Content Engine | Iselune Design</title>
    <style>
        /* Immersive Boho & Celestial Themed Styles */
        body, html {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            background-color: #faf7f2; /* Soft warm linen/cream background */
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            color: #51463e; /* Gentle, earthy charcoal-taupe text */
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* Ambient celestial lighting effect in background corner */
        body::before {
            content: '';
            position: absolute;
            top: -10%;
            right: -10%;
            width: 50%;
            height: 50%;
            background: radial-gradient(circle, rgba(235, 219, 203, 0.4) 0%, rgba(250, 247, 242, 0) 70%);
            z-index: 1;
            pointer-events: none;
        }

        /* Tool Dashboard Container */
        .engine-card {
            background-color: #ffffff; /* Clean white canvas card */
            width: 100%;
            max-width: 540px;
            padding: 45px;
            border-radius: 20px;
            box-shadow: 0 12px 40px rgba(163, 145, 129, 0.12); /* Soft, warm shadow drop */
            border: 1px solid rgba(214, 201, 188, 0.5); /* Delicate taupe border alignment */
            z-index: 2;
            box-sizing: border-box;
            text-align: center;
        }

        /* Header Logo Section Styling */
        .brand-header {
            margin-bottom: 35px;
        }

        /* Responsive container designed explicitly for your vector SVG logo */
        .brand-logo {
            display: block;
            max-width: 160px;      /* Sharp, elegant sizing for your line art */
            height: auto;          /* Scalable vector math preserves layout proportions */
            margin: 0 auto 16px;   /* Centers horizontally and offsets typography below */
        }

        h1 {
            font-family: 'Georgia', serif; /* Luxurious Serif font matching Iselune typography style */
            font-weight: 400;
            font-size: 28px;
            color: #40352e;
            margin: 0 0 8px 0;
            letter-spacing: 0.5px;
        }

        .subtitle {
            font-size: 14px;
            color: #8c7b70;
            margin: 0 0 25px 0;
            line-height: 1.5;
        }

        /* Form Controls Layout */
        .form-group {
            text-align: left;
            margin-bottom: 24px;
        }

        label {
            display: block;
            font-size: 12px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #8c7b70;
            margin-bottom: 8px;
        }

        /* Form Inputs (Dropdowns and Text Areas) */
        select, textarea {
            width: 100%;
            box-sizing: border-box;
            background-color: #faf7f2;
            border: 1px solid #e6ded6;
            border-radius: 10px;
            padding: 14px 16px;
            font-size: 14px;
            color: #51463e;
            outline: none;
            transition: all 0.25s ease;
            font-family: inherit;
        }

        select {
            cursor: pointer;
            appearance: none;
            /* Elegant custom dropdown arrow marker */
            background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg xmlns='http://w3.org' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%238c7b70' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
            background-repeat: no-repeat;
            background-position: right 16px center;
            padding-right: 40px;
        }

        textarea {
            resize: none;
            height: 110px;
            line-height: 1.5;
        }

        textarea::placeholder {
            color: #bcaea1;
            opacity: 0.6;
        }

        /* Input interactive focus state indicators */
        select:focus, textarea:focus {
            border-color: #bfa895; /* Accent taupe tone focus */
            background-color: #ffffff;
            box-shadow: 0 0 0 3px rgba(191, 168, 149, 0.15);
        }

        /* Earthy Premium Action Button */
        .submit-btn {
            width: 100%;
            background-color: #51463e; /* Luxurious dark espresso earthy shade */
            color: #faf7f2;
            border: none;
            border-radius: 10px;
            padding: 16px;
            font-size: 14px;
            font-weight: 600;
            letter-spacing: 1px;
            text-transform: uppercase;
            cursor: pointer;
            transition: all 0.2s ease;
            margin-top: 10px;
            box-shadow: 0 4px 15px rgba(81, 70, 62, 0.2);
        }

        .submit-btn:hover {
            background-color: #40352e;
            transform: translateY(-1px);
            box-shadow: 0 6px 20px rgba(81, 70, 62, 0.3);
        }

        .submit-btn:active {
            transform: translateY(0);
        }
    </style>
</head>
<body>

    <div class="engine-card">
        <!-- Brand Header Section -->
        <div class="brand-header">
            <!-- Programmed directly to call your transparent SVG file -->
            <img class="brand-logo" src="logo.svg" alt="Iselune Design Logo">
            <h1>Aesthetic Content Engine</h1>
            <div class="subtitle">Generate high-converting, luxury social media captions for your templates in seconds.</div>
        </div>

        <!-- Input Interface Matrix -->
        <div class="form-group">
            <label for="template">What template are you using today?</label>
            <select id="template">
                <option>Med Spa & Esthetician</option>
                <option>Yoga Studio & Wellness</option>
                <option>Celestial Jewelry Boutique</option>
                <option>Boho Interior & Decor</option>
            </select>
        </div>

        <div class="form-group">
            <label for="topic">What is the specific topic, announcement, or offer?</label>
            <textarea id="topic" placeholder="e.g., A 10% off flash sale on lip fillers, or Saturday lash openings..."></textarea>
        </div>

        <div class="form-group">
            <label for="tone">What tone of voice should the caption use?</label>
            <select id="tone">
                <option>Luxurious & Elegant</option>
                <option>Mystic & Grounded</option>
                <option>Minimalist & Modern</option>
                <option>Warm & Welcoming</option>
            </select>
        </div>

        <button class="submit-btn">Generate Caption</button>
    </div>

</body>
</html>
