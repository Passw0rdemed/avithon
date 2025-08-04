<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>عين الصقر - منظومة سلامة وأمن الطيران الذكية</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;900&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        :root {
            --primary-color: #5D5CDE;
            --secondary-color: #1e3a8a;
            --accent-color: #fbbf24;
            --success-color: #10b981;
            --warning-color: #f59e0b;
            --danger-color: #ef4444;
            --dark-bg: #0f172a;
            --light-bg: #f8fafc;
            --text-dark: #1e293b;
            --text-light: #64748b;
            --glass-bg: rgba(255, 255, 255, 0.1);
            --glass-border: rgba(255, 255, 255, 0.2);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Cairo', sans-serif;
            background: linear-gradient(135deg, var(--dark-bg) 0%, var(--secondary-color) 100%);
            color: white;
            overflow-x: hidden;
            min-height: 100vh;
        }

        /* Navigation */
        .navbar {
            position: fixed;
            top: 0;
            width: 100%;
            z-index: 1000;
            background: rgba(15, 23, 42, 0.95);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--glass-border);
            padding: 1rem 0;
            transition: all 0.3s ease;
        }

        .nav-container {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 2rem;
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 1rem;
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--primary-color);
        }

        .logo i {
            font-size: 2rem;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.1); }
        }

        .nav-menu {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        .nav-item {
            cursor: pointer;
            padding: 0.5rem 1rem;
            border-radius: 8px;
            transition: all 0.3s ease;
            position: relative;
        }

        .nav-item:hover, .nav-item.active {
            background: var(--primary-color);
            transform: translateY(-2px);
        }

        /* Main Container */
        .container {
            margin-top: 80px;
            padding: 2rem;
            max-width: 1400px;
            margin-left: auto;
            margin-right: auto;
        }

        /* Hero Section */
        .hero {
            text-align: center;
            padding: 4rem 0;
            background: linear-gradient(45deg, var(--primary-color), var(--secondary-color));
            border-radius: 20px;
            margin-bottom: 3rem;
            position: relative;
            overflow: hidden;
        }

        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000"><polygon fill="rgba(255,255,255,0.1)" points="0,1000 1000,0 1000,1000"/></svg>');
            pointer-events: none;
        }

        .hero-content {
            position: relative;
            z-index: 2;
        }

        .hero h1 {
            font-size: 3.5rem;
            font-weight: 900;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .hero p {
            font-size: 1.3rem;
            opacity: 0.9;
            max-width: 800px;
            margin: 0 auto 2rem;
            line-height: 1.6;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }

        .stat-card {
            background: var(--glass-bg);
            backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            border-radius: 15px;
            padding: 2rem;
            text-align: center;
            transition: all 0.3s ease;
        }

        .stat-card:hover {
            transform: translateY(-5px);
            background: rgba(255, 255, 255, 0.15);
        }

        .stat-number {
            font-size: 2.5rem;
            font-weight: 900;
            color: var(--accent-color);
            margin-bottom: 0.5rem;
        }

        .stat-label {
            font-size: 1rem;
            opacity: 0.8;
        }

        /* Dashboard Grid */
        .dashboard {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }

        .dashboard-card {
            background: var(--glass-bg);
            backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            border-radius: 20px;
            padding: 2rem;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .dashboard-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
        }

        .dashboard-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        }

        .card-header {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 2rem;
        }

        .card-icon {
            width: 60px;
            height: 60px;
            background: linear-gradient(135deg, var(--primary-color), var(--accent-color));
            border-radius: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
        }

        .card-title {
            font-size: 1.3rem;
            font-weight: 700;
        }

        /* Alert System */
        .alert-system {
            background: linear-gradient(135deg, var(--danger-color), #dc2626);
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1rem 0;
            border-left: 5px solid #fca5a5;
            animation: alertPulse 2s infinite;
        }

        @keyframes alertPulse {
            0%, 100% { box-shadow: 0 0 20px rgba(239, 68, 68, 0.3); }
            50% { box-shadow: 0 0 30px rgba(239, 68, 68, 0.6); }
        }

        .alert-header {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1rem;
        }

        .alert-icon {
            font-size: 1.5rem;
            animation: bounce 1s infinite;
        }

        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-5px); }
        }

        /* Real-time Data */
        .realtime-data {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 1rem;
            margin: 1rem 0;
        }

        .data-item {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            border: 1px solid var(--glass-border);
        }

        .data-value {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--accent-color);
        }

        .data-label {
            font-size: 0.9rem;
            opacity: 0.8;
            margin-top: 0.5rem;
        }

        /* 3D Visualization Container */
        .visualization-3d {
            height: 400px;
            border-radius: 15px;
            overflow: hidden;
            background: linear-gradient(135deg, #1e3a8a, #3730a3);
            position: relative;
        }

        /* Training Module */
        .training-module {
            background: linear-gradient(135deg, var(--success-color), #059669);
            border-radius: 15px;
            padding: 2rem;
            margin: 1rem 0;
        }

        .training-scenarios {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-top: 1rem;
        }

        .scenario-card {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 1.5rem;
            text-align: center;
            transition: all 0.3s ease;
            cursor: pointer;
        }

        .scenario-card:hover {
            background: rgba(255, 255, 255, 0.2);
            transform: scale(1.05);
        }

        /* Maintenance Prediction */
        .maintenance-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1rem;
            margin: 1rem 0;
        }

        .aircraft-status {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 1.5rem;
            border-left: 5px solid var(--success-color);
        }

        .aircraft-status.warning {
            border-left-color: var(--warning-color);
        }

        .aircraft-status.critical {
            border-left-color: var(--danger-color);
        }

        /* Security Monitor */
        .security-zones {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1rem;
            margin: 1rem 0;
        }

        .zone-status {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            position: relative;
        }

        .zone-indicator {
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background: var(--success-color);
            margin: 0 auto 0.5rem;
            animation: statusBlink 2s infinite;
        }

        .zone-indicator.warning {
            background: var(--warning-color);
        }

        .zone-indicator.critical {
            background: var(--danger-color);
        }

        @keyframes statusBlink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }

        /* Weather Integration */
        .weather-panel {
            background: linear-gradient(135deg, #0ea5e9, #0284c7);
            border-radius: 15px;
            padding: 2rem;
            margin: 1rem 0;
        }

        .weather-conditions {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
            gap: 1rem;
            margin-top: 1rem;
        }

        .weather-item {
            text-align: center;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 1rem;
        }

        .weather-icon {
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }

        /* AI Analytics */
        .ai-insights {
            background: linear-gradient(135deg, #7c3aed, #6d28d9);
            border-radius: 15px;
            padding: 2rem;
            margin: 1rem 0;
        }

        .insight-item {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin: 0.5rem 0;
            border-left: 4px solid var(--accent-color);
        }

        /* Performance Metrics */
        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin: 1rem 0;
        }

        .metric-card {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 1.5rem;
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        .metric-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
        }

        .metric-value {
            font-size: 2rem;
            font-weight: 900;
            color: var(--accent-color);
            margin-bottom: 0.5rem;
        }

        /* Emergency Response */
        .emergency-panel {
            background: linear-gradient(135deg, #ef4444, #dc2626);
            border-radius: 15px;
            padding: 2rem;
            margin: 1rem 0;
            border: 2px solid #fca5a5;
        }

        .emergency-actions {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-top: 1rem;
        }

        .action-button {
            background: rgba(255, 255, 255, 0.2);
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-radius: 10px;
            padding: 1rem;
            color: white;
            cursor: pointer;
            transition: all 0.3s ease;
            text-align: center;
        }

        .action-button:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: scale(1.05);
        }

        /* Modal */
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.8);
            z-index: 2000;
            backdrop-filter: blur(10px);
        }

        .modal-content {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: var(--dark-bg);
            border-radius: 20px;
            padding: 2rem;
            max-width: 600px;
            width: 90%;
            border: 1px solid var(--glass-border);
        }

        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 2rem;
        }

        .close-modal {
            background: none;
            border: none;
            color: white;
            font-size: 1.5rem;
            cursor: pointer;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .nav-menu {
                display: none;
            }
            
            .hero h1 {
                font-size: 2.5rem;
            }
            
            .dashboard {
                grid-template-columns: 1fr;
            }
            
            .stats-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        /* Loading Animation */
        .loading {
            display: inline-block;
            width: 20px;
            height: 20px;
            border: 3px solid rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            border-top-color: var(--accent-color);
            animation: spin 1s ease-in-out infinite;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        /* Scrollbar Styling */
        ::-webkit-scrollbar {
            width: 8px;
        }

        ::-webkit-scrollbar-track {
            background: var(--dark-bg);
        }

        ::-webkit-scrollbar-thumb {
            background: var(--primary-color);
            border-radius: 4px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: var(--accent-color);
        }

        /* Dark mode support */
        .dark {
            --light-bg: #181818;
        }

        /* Airport Markers Styling */
        .airport-marker {
            transition: all 0.3s ease;
        }

        .airport-marker:hover {
            transform: scale(1.1);
        }

        .airport-icon {
            width: 50px;
            height: 50px;
            background: linear-gradient(135deg, var(--primary-color), var(--accent-color));
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.5rem;
            position: relative;
            animation: airportPulse 3s infinite;
            cursor: pointer;
            box-shadow: 0 5px 15px rgba(93, 92, 222, 0.4);
        }

        .airport-pulse {
            position: absolute;
            top: -10px;
            left: -10px;
            right: -10px;
            bottom: -10px;
            border: 2px solid var(--accent-color);
            border-radius: 50%;
            animation: pulse 2s infinite;
            opacity: 0.6;
        }

        @keyframes airportPulse {
            0%, 100% { box-shadow: 0 5px 15px rgba(93, 92, 222, 0.4); }
            50% { box-shadow: 0 5px 25px rgba(93, 92, 222, 0.8); }
        }

        .airport-label {
            position: absolute;
            top: 60px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0, 0, 0, 0.8);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.9rem;
            white-space: nowrap;
            opacity: 0;
            transition: all 0.3s ease;
            pointer-events: none;
        }

        .airport-marker:hover .airport-label {
            opacity: 1;
            top: 55px;
        }

        /* Section Cards */
        .section-content {
            display: none;
        }

        .section-content.active {
            display: block;
        }

        /* Main Map Section Styling */
        .main-map-section {
            text-align: center;
            padding: 2rem 0;
        }

        .map-hero {
            margin-bottom: 3rem;
        }

        .map-hero-content {
            margin-bottom: 3rem;
        }

        .map-title {
            font-size: 4rem;
            font-weight: 900;
            background: linear-gradient(135deg, var(--primary-color), var(--accent-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 1rem;
            text-shadow: 0 4px 8px rgba(0,0,0,0.3);
        }

        .map-subtitle {
            font-size: 1.5rem;
            opacity: 0.9;
            margin-bottom: 1rem;
            line-height: 1.6;
        }

        .map-instruction {
            font-size: 1.1rem;
            color: var(--accent-color);
            font-weight: 600;
            animation: fadeInOut 3s infinite;
        }

        @keyframes fadeInOut {
            0%, 100% { opacity: 0.7; }
            50% { opacity: 1; }
        }

        .overview-stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            margin: 2rem 0;
            max-width: 1000px;
            margin-left: auto;
            margin-right: auto;
        }

        .overview-stat {
            background: var(--glass-bg);
            backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            border-radius: 15px;
            padding: 2rem;
            text-align: center;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .overview-stat::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
        }

        .overview-stat:hover {
            transform: translateY(-5px);
            background: rgba(255, 255, 255, 0.15);
            box-shadow: 0 15px 35px rgba(93, 92, 222, 0.3);
        }

        .overview-stat .stat-number {
            font-size: 2.5rem;
            font-weight: 900;
            color: var(--accent-color);
            margin-bottom: 0.5rem;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }

        .overview-stat .stat-label {
            font-size: 1rem;
            opacity: 0.9;
            font-weight: 600;
        }

        .saudi-map-container {
            max-width: 1200px;
            margin: 0 auto;
            position: relative;
        }

        /* Airport Header Styling */
        .airport-header {
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            border-radius: 20px;
            padding: 2rem;
            margin-bottom: 2rem;
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        .airport-header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000"><polygon fill="rgba(255,255,255,0.1)" points="0,1000 1000,0 1000,1000"/></svg>');
            pointer-events: none;
        }

        .airport-header-content {
            position: relative;
            z-index: 2;
        }

        .airport-title {
            font-size: 2.5rem;
            font-weight: 900;
            margin-bottom: 0.5rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .airport-subtitle {
            font-size: 1.2rem;
            opacity: 0.8;
            margin-bottom: 2rem;
        }

        .airport-stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
        }

        .airport-stat {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 10px;
            padding: 1.5rem;
            text-align: center;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .airport-stat-number {
            font-size: 1.8rem;
            font-weight: 900;
            color: var(--accent-color);
            margin-bottom: 0.5rem;
        }

        .airport-stat-label {
            font-size: 0.9rem;
            opacity: 0.8;
        }

        /* Back to Map Button */
        .back-to-map {
            margin-bottom: 2rem;
        }

        .back-btn {
            background: linear-gradient(135deg, var(--glass-bg), rgba(255, 255, 255, 0.2));
            backdrop-filter: blur(20px);
            border: 2px solid var(--glass-border);
            color: white;
            padding: 1rem 2rem;
            border-radius: 50px;
            cursor: pointer;
            font-size: 1rem;
            font-weight: 600;
            transition: all 0.3s ease;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
        }

        .back-btn:hover {
            background: linear-gradient(135deg, var(--primary-color), var(--accent-color));
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(93, 92, 222, 0.4);
        }

        .back-btn i {
            transition: transform 0.3s ease;
        }

        .back-btn:hover i {
            transform: translateX(5px);
        }
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="nav-container">
            <div class="logo">
                <i class="fas fa-eye"></i>
                <span>عين الصقر</span>
            </div>
            <ul class="nav-menu">
                <li class="nav-item active" onclick="showSection('dashboard')">لوحة التحكم</li>
                <li class="nav-item" onclick="showSection('security')">الأمن</li>
                <li class="nav-item" onclick="showSection('safety')">السلامة</li>
                <li class="nav-item" onclick="showSection('analytics')">التحليلات</li>
                <li class="nav-item" onclick="showSection('training')">التدريب</li>
                <li class="nav-item" onclick="showSection('reports')">التقارير</li>
            </ul>
        </div>
    </nav>

    <div class="container">
        <!-- Main Map Section - Default View -->
        <section id="main-map" class="main-map-section">
            <div class="map-hero">
                <div class="map-hero-content">
                    <h1 class="map-title">عين الصقر</h1>
                    <p class="map-subtitle">منظومة ذكية متكاملة لتعزيز أمن وسلامة قطاع الطيران</p>
                    <p class="map-instruction">اضغط على أي مطار لعرض لوحة التحكم المخصصة له</p>
                </div>
                
                <div class="overview-stats">
                    <div class="overview-stat">
                        <div class="stat-number">4</div>
                        <div class="stat-label">مطارات محمية</div>
                    </div>
                    <div class="overview-stat">
                        <div class="stat-number">666</div>
                        <div class="stat-label">رحلة يومياً</div>
                    </div>
                    <div class="overview-stat">
                        <div class="stat-number">32,457</div>
                        <div class="stat-label">مسافر يومياً</div>
                    </div>
                    <div class="overview-stat">
                        <div class="stat-number">99.8%</div>
                        <div class="stat-label">معدل كشف التهديدات</div>
                    </div>
                </div>
            </div>
            
            <div class="saudi-map-container">
                <div id="saudi-arabia-map" style="position: relative; width: 100%; height: 700px; background: linear-gradient(135deg, #1e3a8a, #3730a3); border-radius: 20px; overflow: hidden; box-shadow: 0 25px 50px rgba(0,0,0,0.3);">
                    <!-- Saudi Arabia Accurate Real Map SVG -->
                    <svg viewBox="0 0 1200 800" style="width: 100%; height: 100%;">
                        <!-- تعريف المكونات -->
                        <defs>
                            <!-- تدرج للخلفية -->
                            <linearGradient id="mapGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" style="stop-color:#1e3a8a;stop-opacity:0.1"/>
                                <stop offset="100%" style="stop-color:#3730a3;stop-opacity:0.1"/>
                            </linearGradient>
                            
                            <!-- نمط للصحراء -->
                            <pattern id="desertPattern" patternUnits="userSpaceOnUse" width="15" height="15">
                                <circle cx="7.5" cy="7.5" r="1" fill="rgba(255,215,0,0.2)"/>
                                <circle cx="3" cy="3" r="0.5" fill="rgba(255,215,0,0.1)"/>
                                <circle cx="12" cy="12" r="0.5" fill="rgba(255,215,0,0.1)"/>
                            </pattern>
                            
                            <!-- نمط الجبال -->
                            <pattern id="mountainPattern" patternUnits="userSpaceOnUse" width="20" height="20">
                                <polygon points="0,20 10,5 20,20" fill="rgba(139,69,19,0.2)"/>
                            </pattern>
                            
                            <!-- تأثير توهج للحدود -->
                            <filter id="glow">
                                <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
                                <feMerge> 
                                    <feMergeNode in="coloredBlur"/>
                                    <feMergeNode in="SourceGraphic"/>
                                </feMerge>
                            </filter>
                        </defs>
                        
                        <!-- الحدود الحقيقية للمملكة العربية السعودية -->
                        <path d="M200 150 
                                 L230 120 
                                 L260 110 
                                 L290 105 
                                 L320 100 
                                 L350 95 
                                 L380 90 
                                 L410 85 
                                 L450 80 
                                 L490 78 
                                 L530 75 
                                 L570 73 
                                 L610 70 
                                 L650 68 
                                 L690 65 
                                 L730 63 
                                 L770 60 
                                 L810 58 
                                 L850 55 
                                 L890 53 
                                 L930 50 
                                 L970 48 
                                 L1000 45 
                                 L1020 50 
                                 L1030 55 
                                 L1035 65 
                                 L1040 75 
                                 L1042 85 
                                 L1045 95 
                                 L1047 105 
                                 L1048 115 
                                 L1050 125 
                                 L1051 135 
                                 L1052 145 
                                 L1053 155 
                                 L1054 165 
                                 L1055 175 
                                 L1056 185 
                                 L1057 195 
                                 L1058 205 
                                 L1059 215 
                                 L1060 225 
                                 L1061 235 
                                 L1062 245 
                                 L1063 255 
                                 L1064 265 
                                 L1065 275 
                                 L1066 285 
                                 L1067 295 
                                 L1068 305 
                                 L1069 315 
                                 L1070 325 
                                 L1071 335 
                                 L1072 345 
                                 L1073 355 
                                 L1074 365 
                                 L1075 375 
                                 L1076 385 
                                 L1077 395 
                                 L1078 405 
                                 L1079 415 
                                 L1080 425 
                                 L1081 435 
                                 L1082 445 
                                 L1083 455 
                                 L1084 465 
                                 L1085 475 
                                 L1086 485 
                                 L1087 495 
                                 L1088 505 
                                 L1089 515 
                                 L1090 525 
                                 L1091 535 
                                 L1092 545 
                                 L1093 555 
                                 L1094 565 
                                 L1095 575 
                                 L1090 585 
                                 L1085 595 
                                 L1075 605 
                                 L1065 615 
                                 L1050 620 
                                 L1030 625 
                                 L1010 630 
                                 L990 635 
                                 L970 640 
                                 L950 645 
                                 L930 650 
                                 L910 655 
                                 L890 660 
                                 L870 665 
                                 L850 670 
                                 L830 675 
                                 L810 680 
                                 L790 685 
                                 L770 690 
                                 L750 695 
                                 L730 700 
                                 L710 705 
                                 L690 710 
                                 L670 715 
                                 L650 720 
                                 L630 725 
                                 L610 730 
                                 L590 735 
                                 L570 740 
                                 L550 745 
                                 L530 750 
                                 L510 755 
                                 L490 760 
                                 L470 765 
                                 L450 770 
                                 L430 770 
                                 L410 770 
                                 L390 765 
                                 L370 760 
                                 L350 755 
                                 L330 750 
                                 L310 745 
                                 L290 740 
                                 L270 735 
                                 L250 730 
                                 L230 725 
                                 L210 720 
                                 L190 715 
                                 L170 710 
                                 L150 705 
                                 L130 700 
                                 L110 695 
                                 L90 690 
                                 L70 680 
                                 L50 670 
                                 L35 660 
                                 L25 650 
                                 L20 640 
                                 L18 630 
                                 L17 620 
                                 L16 610 
                                 L15 600 
                                 L14 590 
                                 L13 580 
                                 L12 570 
                                 L11 560 
                                 L10 550 
                                 L9 540 
                                 L8 530 
                                 L7 520 
                                 L6 510 
                                 L5 500 
                                 L4 490 
                                 L3 480 
                                 L2 470 
                                 L1 460 
                                 L0 450 
                                 L1 440 
                                 L2 430 
                                 L3 420 
                                 L4 410 
                                 L5 400 
                                 L6 390 
                                 L7 380 
                                 L8 370 
                                 L9 360 
                                 L10 350 
                                 L11 340 
                                 L12 330 
                                 L13 320 
                                 L14 310 
                                 L15 300 
                                 L16 290 
                                 L17 280 
                                 L18 270 
                                 L20 260 
                                 L25 250 
                                 L30 240 
                                 L35 230 
                                 L40 220 
                                 L45 210 
                                 L50 200 
                                 L60 190 
                                 L70 180 
                                 L85 170 
                                 L100 160 
                                 L120 155 
                                 L140 152 
                                 L160 150 
                                 L180 150 
                                 L200 150 Z" 
                              fill="rgba(255,255,255,0.15)" 
                              stroke="rgba(255,255,255,0.6)" 
                              stroke-width="3"
                              filter="url(#glow)"/>
                        
                        <!-- البحر الأحمر -->
                        <path d="M0 200 L50 180 L70 200 L90 220 L110 240 L130 260 L150 280 L170 300 L190 320 L210 340 L230 360 L250 380 L270 400 L290 420 L310 440 L330 460 L350 480 L370 500 L390 520 L410 540 L430 560 L450 580 L470 600 L490 620 L510 640 L530 660 L550 680 L570 700 L590 720 L610 740 L630 760 L650 780 L670 800 L0 800 Z" 
                              fill="rgba(30, 144, 255, 0.4)" 
                              stroke="rgba(30, 144, 255, 0.7)" 
                              stroke-width="2"/>
                        
                        <!-- الخليج العربي -->
                        <path d="M1100 200 L1090 220 L1080 240 L1070 260 L1060 280 L1050 300 L1040 320 L1030 340 L1020 360 L1010 380 L1000 400 L990 420 L980 440 L970 460 L960 480 L950 500 L940 520 L930 540 L920 560 L910 580 L900 600 L890 620 L880 640 L870 660 L860 680 L850 700 L840 720 L830 740 L820 760 L810 780 L800 800 L1200 800 L1200 0 L1100 200 Z" 
                              fill="rgba(30, 144, 255, 0.4)" 
                              stroke="rgba(30, 144, 255, 0.7)" 
                              stroke-width="2"/>
                        
                        <!-- الربع الخالي -->
                        <path d="M400 550 L500 570 L600 580 L700 590 L800 600 L850 620 L880 640 L900 660 L920 680 L940 700 L960 720 L980 740 L1000 760 L900 770 L800 780 L700 785 L600 790 L500 780 L400 770 L350 750 L320 720 L300 690 L290 660 L300 630 L320 600 L350 580 L380 565 Z" 
                              fill="url(#desertPattern)" 
                              stroke="rgba(255,215,0,0.3)" 
                              stroke-width="1"/>
                        
                        <!-- جبال الحجاز -->
                        <path d="M80 180 L120 170 L160 175 L200 180 L240 185 L280 190 L320 195 L360 200 L400 205 L440 210 L400 250 L360 290 L320 330 L280 370 L240 410 L200 450 L160 490 L120 530 L80 570 L50 550 L30 520 L20 490 L15 460 L12 430 L10 400 L8 370 L6 340 L4 310 L2 280 L0 250 L10 220 L30 200 L50 185 Z" 
                              fill="url(#mountainPattern)" 
                              stroke="rgba(139,69,19,0.5)" 
                              stroke-width="1"/>
                        
                        <!-- خطوط الطول والعرض -->
                        <line x1="0" y1="400" x2="1200" y2="400" stroke="rgba(255,255,255,0.1)" stroke-width="1" stroke-dasharray="5,5"/>
                        <line x1="600" y1="0" x2="600" y2="800" stroke="rgba(255,255,255,0.1)" stroke-width="1" stroke-dasharray="5,5"/>
                        
                        <!-- Labels للمناطق الجغرافية -->
                        <text x="100" y="450" fill="rgba(255,255,255,0.8)" font-size="14" text-anchor="middle" font-weight="bold">البحر الأحمر</text>
                        <text x="650" y="680" fill="rgba(255,255,255,0.8)" font-size="14" text-anchor="middle" font-weight="bold">الربع الخالي</text>
                        <text x="1050" y="450" fill="rgba(255,255,255,0.8)" font-size="14" text-anchor="middle" font-weight="bold">الخليج العربي</text>
                        <text x="200" y="350" fill="rgba(255,255,255,0.8)" font-size="14" text-anchor="middle" font-weight="bold">جبال الحجاز</text>
                        
                        <!-- المدن الرئيسية -->
                        <text x="600" y="380" fill="white" font-size="18" text-anchor="middle" font-weight="bold">الرياض</text>
                        <text x="200" y="480" fill="white" font-size="18" text-anchor="middle" font-weight="bold">جدة</text>
                        <text x="250" y="300" fill="white" font-size="18" text-anchor="middle" font-weight="bold">المدينة المنورة</text>
                        <text x="950" y="420" fill="white" font-size="18" text-anchor="middle" font-weight="bold">الدمام</text>
                        
                        <!-- المدن الثانوية -->
                        <text x="350" y="220" fill="rgba(255,255,255,0.9)" font-size="14" text-anchor="middle">تبوك</text>
                        <text x="500" y="280" fill="rgba(255,255,255,0.9)" font-size="14" text-anchor="middle">حائل</text>
                        <text x="300" y="400" fill="rgba(255,255,255,0.9)" font-size="14" text-anchor="middle">مكة المكرمة</text>
                        <text x="450" y="520" fill="rgba(255,255,255,0.9)" font-size="14" text-anchor="middle">الطائف</text>
                        <text x="550" y="620" fill="rgba(255,255,255,0.9)" font-size="14" text-anchor="middle">أبها</text>
                        <text x="850" y="520" fill="rgba(255,255,255,0.9)" font-size="14" text-anchor="middle">الأحساء</text>
                        <text x="750" y="320" fill="rgba(255,255,255,0.9)" font-size="14" text-anchor="middle">القصيم</text>
                        <text x="400" y="650" fill="rgba(255,255,255,0.9)" font-size="14" text-anchor="middle">جيزان</text>
                        
                        <!-- البوصلة المحسنة -->
                        <g transform="translate(1050, 120)">
                            <circle cx="0" cy="0" r="40" fill="rgba(0,0,0,0.7)" stroke="rgba(255,255,255,0.5)" stroke-width="2"/>
                            <circle cx="0" cy="0" r="35" fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="1"/>
                            <circle cx="0" cy="0" r="30" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
                            
                            <!-- سهم الشمال -->
                            <polygon points="0,-35 5,-25 0,-15 -5,-25" fill="#fbbf24"/>
                            <polygon points="0,15 5,25 0,35 -5,25" fill="rgba(255,255,255,0.5)"/>
                            
                            <!-- علامات الاتجاهات -->
                            <text x="0" y="-20" fill="white" font-size="14" text-anchor="middle" font-weight="bold">ش</text>
                            <text x="25" y="5" fill="white" font-size="12" text-anchor="middle">ق</text>
                            <text x="0" y="30" fill="white" font-size="12" text-anchor="middle">ج</text>
                            <text x="-25" y="5" fill="white" font-size="12" text-anchor="middle">غ</text>
                            
                            <!-- النقاط الفرعية -->
                            <circle cx="18" cy="-18" r="2" fill="rgba(255,255,255,0.6)"/>
                            <circle cx="18" cy="18" r="2" fill="rgba(255,255,255,0.6)"/>
                            <circle cx="-18" cy="18" r="2" fill="rgba(255,255,255,0.6)"/>
                            <circle cx="-18" cy="-18" r="2" fill="rgba(255,255,255,0.6)"/>
                        </g>
                    </svg>
                    
                    <!-- Airport locations based on precise GeoJSON coordinates -->
                    
                    <!-- مطار الملك خالد الدولي - الرياض -->
                    <!-- Coordinates: 24.9576, 46.6988 (Center of Saudi Arabia) -->
                    <div class="airport-marker" data-airport="riyadh" data-lat="24.9576" data-lng="46.6988" style="position: absolute; top: 47.2%; left: 50.8%; cursor: pointer;">
                        <div class="airport-icon">
                            <i class="fas fa-plane-departure"></i>
                            <div class="airport-pulse"></div>
                        </div>
                        <div class="airport-label">
                            مطار الملك خالد الدولي<br>
                            <small>الرياض - العاصمة</small><br>
                            <small style="opacity: 0.7;">24.9576°N, 46.6988°E</small>
                        </div>
                    </div>
                    
                    <!-- مطار الملك عبدالعزيز الدولي - جدة -->
                    <!-- Coordinates: 21.6702, 39.1513 (Western coast, Red Sea) -->
                    <div class="airport-marker" data-airport="jeddah" data-lat="21.6702" data-lng="39.1513" style="position: absolute; top: 63.8%; left: 16.2%; cursor: pointer;">
                        <div class="airport-icon">
                            <i class="fas fa-plane-departure"></i>
                            <div class="airport-pulse"></div>
                        </div>
                        <div class="airport-label">
                            مطار الملك عبدالعزيز الدولي<br>
                            <small>جدة - بوابة الحرمين</small><br>
                            <small style="opacity: 0.7;">21.6702°N, 39.1513°E</small>
                        </div>
                    </div>
                    
                    <!-- مطار الأمير محمد بن عبدالعزيز - المدينة المنورة -->
                    <!-- Coordinates: 24.5534, 39.7051 (Northwest, near Medina) -->
                    <div class="airport-marker" data-airport="madinah" data-lat="24.5534" data-lng="39.7051" style="position: absolute; top: 48.5%; left: 19.1%; cursor: pointer;">
                        <div class="airport-icon">
                            <i class="fas fa-plane-departure"></i>
                            <div class="airport-pulse"></div>
                        </div>
                        <div class="airport-label">
                            مطار الأمير محمد بن عبدالعزيز<br>
                            <small>المدينة المنورة</small><br>
                            <small style="opacity: 0.7;">24.5534°N, 39.7051°E</small>
                        </div>
                    </div>
                    
                    <!-- مطار الملك فهد الدولي - الدمام -->
                    <!-- Coordinates: 26.4711, 49.7979 (Eastern coast, Persian Gulf) -->
                    <div class="airport-marker" data-airport="dammam" data-lat="26.4711" data-lng="49.7979" style="position: absolute; top: 42.1%; left: 80.5%; cursor: pointer;">
                        <div class="airport-icon">
                            <i class="fas fa-plane-departure"></i>
                            <div class="airport-pulse"></div>
                        </div>
                        <div class="airport-label">
                            مطار الملك فهد الدولي<br>
                            <small>الدمام - المنطقة الشرقية</small><br>
                            <small style="opacity: 0.7;">26.4711°N, 49.7979°E</small>
                        </div>
                    </div>
                    
                    <!-- لوحة المعلومات الجغرافية -->
                    <div style="position: absolute; bottom: 20px; left: 20px; background: rgba(0,0,0,0.8); padding: 1.5rem; border-radius: 15px; font-size: 13px; border: 1px solid rgba(255,255,255,0.2);">
                        <div style="color: #fbbf24; font-weight: bold; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem;">
                            <i class="fas fa-globe-americas"></i> المملكة العربية السعودية
                        </div>
                        <div style="color: rgba(255,255,255,0.9); line-height: 1.6;">
                            <div><strong>المساحة:</strong> 2,149,690 كم²</div>
                            <div><strong>السكان:</strong> 35 مليون نسمة</div>
                            <div><strong>المطارات الدولية:</strong> 27 مطار</div>
                            <div><strong>المطارات المحمية:</strong> 4 مطارات رئيسية</div>
                            <div><strong>المناطق:</strong> 13 منطقة إدارية</div>
                        </div>
                    </div>
                    
                    <!-- مؤشر الحالة العامة المحسن -->
                    <div style="position: absolute; top: 20px; right: 20px; background: linear-gradient(135deg, rgba(16, 185, 129, 0.9), rgba(5, 150, 105, 0.9)); padding: 1rem 1.5rem; border-radius: 50px; font-size: 14px; font-weight: bold; box-shadow: 0 5px 15px rgba(16, 185, 129, 0.3); border: 1px solid rgba(255,255,255,0.2);">
                        <i class="fas fa-shield-check" style="margin-left: 0.5rem;"></i> جميع المطارات آمنة
                    </div>
                    
                    <!-- إحصائيات سريعة -->
                    <div style="position: absolute; top: 20px; left: 20px; background: rgba(0,0,0,0.7); padding: 1rem; border-radius: 10px; font-size: 12px; border: 1px solid rgba(255,255,255,0.2);">
                        <div style="color: #fbbf24; font-weight: bold; margin-bottom: 0.5rem;">
                            <i class="fas fa-chart-line"></i> إحصائيات اليوم
                        </div>
                        <div style="color: rgba(255,255,255,0.9);">
                            <div>الرحلات النشطة: 342</div>
                            <div>المسافرون: 28,567</div>
                            <div>معدل الأمان: 99.8%</div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Airport Dashboard Section -->
        <section id="airport-dashboard" style="display: none;">
            <!-- Back to Map Button -->
            <div class="back-to-map">
                <button onclick="showMainMap()" class="back-btn">
                    <i class="fas fa-arrow-right"></i>
                    العودة للخريطة الرئيسية
                </button>
            </div>

            <!-- Airport Header -->
            <div id="airport-header" class="airport-header">
                <!-- Dynamic content will be inserted here -->
            </div>

            <!-- Airport-Specific Dashboard -->
            <div id="airport-specific-dashboard">
                <!-- Content will be shown based on active navigation -->
            </div>
        </section>

        <!-- Main Dashboard -->
        <section id="dashboard" class="dashboard">
            <!-- Real-time Monitoring -->
            <div class="dashboard-card">
                <div class="card-header">
                    <div class="card-icon">
                        <i class="fas fa-radar-dish"></i>
                    </div>
                    <div>
                        <h3 class="card-title">المراقبة في الوقت الحقيقي</h3>
                        <p>نظام مراقبة ذكي متصل بجميع المطارات</p>
                    </div>
                </div>
                
                <div class="realtime-data">
                    <div class="data-item">
                        <div class="data-value" id="active-flights">342</div>
                        <div class="data-label">رحلات نشطة</div>
                    </div>
                    <div class="data-item">
                        <div class="data-value" id="passengers-today">28,567</div>
                        <div class="data-label">مسافرين اليوم</div>
                    </div>
                    <div class="data-item">
                        <div class="data-value" id="security-alerts">2</div>
                        <div class="data-label">تنبيهات أمنية</div>
                    </div>
                </div>

                <canvas id="flightChart" width="400" height="200"></canvas>
            </div>

            <!-- AI-Powered Security -->
            <div class="dashboard-card">
                <div class="card-header">
                    <div class="card-icon">
                        <i class="fas fa-shield-alt"></i>
                    </div>
                    <div>
                        <h3 class="card-title">الأمن الذكي</h3>
                        <p>كشف التهديدات باستخدام الذكاء الاصطناعي</p>
                    </div>
                </div>

                <div class="security-zones">
                    <div class="zone-status">
                        <div class="zone-indicator"></div>
                        <div>المنطقة الأمنية أ</div>
                        <small>آمن</small>
                    </div>
                    <div class="zone-status">
                        <div class="zone-indicator warning"></div>
                        <div>المنطقة الأمنية ب</div>
                        <small>تحت المراقبة</small>
                    </div>
                    <div class="zone-status">
                        <div class="zone-indicator"></div>
                        <div>المنطقة الأمنية ج</div>
                        <small>آمن</small>
                    </div>
                </div>

                <div class="alert-system">
                    <div class="alert-header">
                        <i class="fas fa-exclamation-triangle alert-icon"></i>
                        <strong>تنبيه أمني</strong>
                    </div>
                    <p>تم رصد حركة غير اعتيادية في البوابة 12 - تم تحويل للفريق الأمني</p>
                </div>

                <canvas id="securityChart" width="400" height="200"></canvas>
            </div>

            <!-- Predictive Maintenance -->
            <div class="dashboard-card">
                <div class="card-header">
                    <div class="card-icon">
                        <i class="fas fa-tools"></i>
                    </div>
                    <div>
                        <h3 class="card-title">الصيانة التنبؤية</h3>
                        <p>توقع الأعطال قبل حدوثها</p>
                    </div>
                </div>

                <div class="maintenance-grid">
                    <div class="aircraft-status">
                        <h4>الطائرة SV-101</h4>
                        <p>الحالة: ممتازة</p>
                        <p>الصيانة التالية: 15 يوم</p>
                    </div>
                    <div class="aircraft-status warning">
                        <h4>الطائرة SV-202</h4>
                        <p>الحالة: تحتاج انتباه</p>
                        <p>مشكلة محتملة في المحرك</p>
                    </div>
                    <div class="aircraft-status critical">
                        <h4>الطائرة SV-303</h4>
                        <p>الحالة: صيانة فورية</p>
                        <p>مطلوب فحص عاجل</p>
                    </div>
                </div>

                <canvas id="maintenanceChart" width="400" height="200"></canvas>
            </div>

            <!-- Weather Integration -->
            <div class="dashboard-card">
                <div class="card-header">
                    <div class="card-icon">
                        <i class="fas fa-cloud-sun"></i>
                    </div>
                    <div>
                        <h3 class="card-title">المراقبة الجوية</h3>
                        <p>تكامل بيانات الطقس مع التشغيل</p>
                    </div>
                </div>

                <div class="weather-panel">
                    <h4>الأحوال الجوية الحالية</h4>
                    <div class="weather-conditions">
                        <div class="weather-item">
                            <div class="weather-icon">☀️</div>
                            <div>الرياض</div>
                            <div>32°س</div>
                        </div>
                        <div class="weather-item">
                            <div class="weather-icon">⛅</div>
                            <div>جدة</div>
                            <div>28°س</div>
                        </div>
                        <div class="weather-item">
                            <div class="weather-icon">🌪️</div>
                            <div>الدمام</div>
                            <div>عاصفة رملية</div>
                        </div>
                    </div>
                </div>

                <canvas id="weatherChart" width="400" height="200"></canvas>
            </div>

            <!-- 3D Airport Visualization -->
            <div class="dashboard-card">
                <div class="card-header">
                    <div class="card-icon">
                        <i class="fas fa-cube"></i>
                    </div>
                    <div>
                        <h3 class="card-title">محاكاة ثلاثية الأبعاد</h3>
                        <p>عرض تفاعلي للمطار</p>
                    </div>
                </div>

                <div class="visualization-3d" id="airport3d">
                    <canvas id="threeCanvas"></canvas>
                </div>
            </div>

            <!-- AI Analytics -->
            <div class="dashboard-card">
                <div class="card-header">
                    <div class="card-icon">
                        <i class="fas fa-brain"></i>
                    </div>
                    <div>
                        <h3 class="card-title">تحليلات الذكاء الاصطناعي</h3>
                        <p>رؤى ذكية وتوصيات آلية</p>
                    </div>
                </div>

                <div class="ai-insights">
                    <h4>التوصيات الذكية</h4>
                    <div class="insight-item">
                        <i class="fas fa-lightbulb"></i>
                        يُنصح بزيادة الطواقم الأمنية في البوابات 5-8 خلال الساعتين القادمتين
                    </div>
                    <div class="insight-item">
                        <i class="fas fa-chart-line"></i>
                        معدل التأخير انخفض بنسبة 23% بعد تطبيق النظام الذكي
                    </div>
                    <div class="insight-item">
                        <i class="fas fa-shield-check"></i>
                        تم منع 15 حادثة أمنية محتملة هذا الأسبوع
                    </div>
                </div>

                <canvas id="aiChart" width="400" height="200"></canvas>
            </div>
        </section>

        <!-- Training Module -->
        <section id="training" style="display: none;">
            <div class="dashboard-card">
                <div class="card-header">
                    <div class="card-icon">
                        <i class="fas fa-graduation-cap"></i>
                    </div>
                    <div>
                        <h3 class="card-title">منصة التدريب الذكي</h3>
                        <p>تدريب الطواقم باستخدام الواقع الافتراضي والمعزز</p>
                    </div>
                </div>

                <div class="training-module">
                    <h4>سيناريوهات التدريب المتاحة</h4>
                    <div class="training-scenarios">
                        <div class="scenario-card" onclick="startTraining('fire')">
                            <i class="fas fa-fire"></i>
                            <h5>حريق في الطائرة</h5>
                            <p>محاكاة التعامل مع الحرائق</p>
                        </div>
                        <div class="scenario-card" onclick="startTraining('security')">
                            <i class="fas fa-user-secret"></i>
                            <h5>تهديد أمني</h5>
                            <p>التعامل مع التهديدات الأمنية</p>
                        </div>
                        <div class="scenario-card" onclick="startTraining('medical')">
                            <i class="fas fa-heart"></i>
                            <h5>طوارئ طبية</h5>
                            <p>الإسعافات الأولية</p>
                        </div>
                        <div class="scenario-card" onclick="startTraining('evacuation')">
                            <i class="fas fa-running"></i>
                            <h5>إخلاء الطائرة</h5>
                            <p>إجراءات الإخلاء السريع</p>
                        </div>
                    </div>
                </div>

                <div class="metrics-grid">
                    <div class="metric-card">
                        <div class="metric-value">847</div>
                        <div class="metric-label">موظف مدرب</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-value">95%</div>
                        <div class="metric-label">معدل النجاح</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-value">156</div>
                        <div class="metric-label">ساعة تدريب</div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Security Section -->
        <section id="security" style="display: none;" class="dashboard">
            <div class="dashboard-card">
                <div class="card-header">
                    <div class="card-icon">
                        <i class="fas fa-shield-alt"></i>
                    </div>
                    <div>
                        <h3 class="card-title">نظام الأمن المتقدم</h3>
                        <p>مراقبة شاملة ودقيقة للتهديدات الأمنية</p>
                    </div>
                </div>
                
                <div class="security-zones">
                    <div class="zone-status">
                        <div class="zone-indicator"></div>
                        <div>منطقة المغادرة</div>
                        <small>آمن - لا توجد تهديدات</small>
                    </div>
                    <div class="zone-status">
                        <div class="zone-indicator warning"></div>
                        <div>منطقة الوصول</div>
                        <small>تحت المراقبة - كثافة عالية</small>
                    </div>
                    <div class="zone-status">
                        <div class="zone-indicator"></div>
                        <div>الساحة الجوية</div>
                        <small>آمن - العمليات طبيعية</small>
                    </div>
                </div>

                <div class="ai-insights">
                    <h4>تحليلات الأمن الذكي</h4>
                    <div class="insight-item">
                        <i class="fas fa-camera"></i>
                        587 كاميرا مراقبة نشطة مع تحليل سلوكي
                    </div>
                    <div class="insight-item">
                        <i class="fas fa-user-check"></i>
                        معدل الفحص الدقيق: 99.7% بدون إنذارات كاذبة
                    </div>
                    <div class="insight-item">
                        <i class="fas fa-search"></i>
                        تم فحص 15,432 راكب اليوم بنجاح
                    </div>
                </div>
            </div>

            <div class="dashboard-card">
                <div class="card-header">
                    <div class="card-icon">
                        <i class="fas fa-robot"></i>
                    </div>
                    <div>
                        <h3 class="card-title">الكشف الذكي للتهديدات</h3>
                        <p>نظام الذكاء الاصطناعي لكشف الأنماط المشبوهة</p>
                    </div>
                </div>

                <div class="metrics-grid">
                    <div class="metric-card">
                        <div class="metric-value">12</div>
                        <div class="metric-label">تهديد تم منعه اليوم</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-value">0.2%</div>
                        <div class="metric-label">معدل الإنذارات الكاذبة</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-value">38s</div>
                        <div class="metric-label">متوسط زمن الاستجابة</div>
                    </div>
                </div>

                <canvas id="securityAnalyticsChart" width="400" height="200"></canvas>
            </div>
        </section>

        <!-- Safety Section -->
        <section id="safety" style="display: none;" class="dashboard">
            <div class="dashboard-card">
                <div class="card-header">
                    <div class="card-icon">
                        <i class="fas fa-heart-pulse"></i>
                    </div>
                    <div>
                        <h3 class="card-title">منظومة السلامة التشغيلية</h3>
                        <p>مراقبة وصيانة تنبؤية لضمان أعلى معايير السلامة</p>
                    </div>
                </div>

                <div class="maintenance-grid">
                    <div class="aircraft-status">
                        <h4>الطائرة SV-101</h4>
                        <p><strong>الحالة:</strong> ممتازة ✅</p>
                        <p><strong>آخر فحص:</strong> 2024-01-15</p>
                        <p><strong>الصيانة التالية:</strong> 15 يوم</p>
                        <p><strong>ساعات الطيران:</strong> 1,247 ساعة</p>
                    </div>
                    <div class="aircraft-status warning">
                        <h4>الطائرة SV-202</h4>
                        <p><strong>الحالة:</strong> تحتاج انتباه ⚠️</p>
                        <p><strong>التنبيه:</strong> مشكلة محتملة في المحرك الأيسر</p>
                        <p><strong>الإجراء:</strong> فحص مجدول خلال 48 ساعة</p>
                        <p><strong>مستوى الخطر:</strong> منخفض</p>
                    </div>
                    <div class="aircraft-status critical">
                        <h4>الطائرة SV-303</h4>
                        <p><strong>الحالة:</strong> صيانة فورية 🔴</p>
                        <p><strong>المشكلة:</strong> انخفاض ضغط النظام الهيدروليكي</p>
                        <p><strong>الإجراء:</strong> توقف فوري للفحص</p>
                        <p><strong>مستوى الخطر:</strong> عالي</p>
                    </div>
                </div>

                <div class="ai-insights">
                    <h4>التنبؤات الذكية للسلامة</h4>
                    <div class="insight-item">
                        <i class="fas fa-chart-line"></i>
                        انخفاض الحوادث بنسبة 34% مقارنة بالعام الماضي
                    </div>
                    <div class="insight-item">
                        <i class="fas fa-tools"></i>
                        96% من الأعطال تم توقعها ومنعها قبل الحدوث
                    </div>
                    <div class="insight-item">
                        <i class="fas fa-clock"></i>
                        متوسط زمن الصيانة انخفض إلى 4.2 ساعة
                    </div>
                </div>
            </div>

            <div class="dashboard-card">
                <div class="card-header">
                    <div class="card-icon">
                        <i class="fas fa-clipboard-check"></i>
                    </div>
                    <div>
                        <h3 class="card-title">مؤشرات الأداء الرئيسية</h3>
                        <p>قياس وتحليل معايير السلامة الحرجة</p>
                    </div>
                </div>

                <div class="metrics-grid">
                    <div class="metric-card">
                        <div class="metric-value">0.01</div>
                        <div class="metric-label">حوادث لكل مليون رحلة</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-value">99.8%</div>
                        <div class="metric-label">معدل الجاهزية التشغيلية</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-value">87%</div>
                        <div class="metric-label">تغطية الصيانة التنبؤية</div>
                    </div>
                </div>

                <canvas id="safetyChart" width="400" height="200"></canvas>
            </div>
        </section>

        <!-- Analytics Section -->
        <section id="analytics" style="display: none;" class="dashboard">
            <div class="dashboard-card">
                <div class="card-header">
                    <div class="card-icon">
                        <i class="fas fa-chart-bar"></i>
                    </div>
                    <div>
                        <h3 class="card-title">تحليلات الأداء الشاملة</h3>
                        <p>رؤى عميقة مدعومة بالذكاء الاصطناعي</p>
                    </div>
                </div>

                <div class="realtime-data">
                    <div class="data-item">
                        <div class="data-value">847M</div>
                        <div class="data-label">نقطة بيانات معالجة</div>
                    </div>
                    <div class="data-item">
                        <div class="data-value">156</div>
                        <div class="data-label">نموذج ذكي نشط</div>
                    </div>
                    <div class="data-item">
                        <div class="data-value">98.7%</div>
                        <div class="data-label">دقة التنبؤات</div>
                    </div>
                    <div class="data-item">
                        <div class="data-value">2.3s</div>
                        <div class="data-label">زمن تحليل البيانات</div>
                    </div>
                </div>

                <canvas id="analyticsChart" width="400" height="300"></canvas>
            </div>

            <div class="dashboard-card">
                <div class="card-header">
                    <div class="card-icon">
                        <i class="fas fa-brain"></i>
                    </div>
                    <div>
                        <h3 class="card-title">التوصيات الذكية</h3>
                        <p>اقتراحات مبنية على تحليل البيانات المتقدم</p>
                    </div>
                </div>

                <div class="ai-insights">
                    <h4>رؤى تشغيلية ذكية</h4>
                    <div class="insight-item">
                        <i class="fas fa-users"></i>
                        توقع زيادة الازدحام في بوابات 5-8 بنسبة 23% خلال الساعتين القادمتين
                    </div>
                    <div class="insight-item">
                        <i class="fas fa-weather-wind"></i>
                        رياح قوية متوقعة في الدمام - يُنصح بتأجيل 3 رحلات
                    </div>
                    <div class="insight-item">
                        <i class="fas fa-cog"></i>
                        نموذج جديد للتنبؤ بالصيانة حقق دقة 97.3% في الاختبارات
                    </div>
                    <div class="insight-item">
                        <i class="fas fa-shield-check"></i>
                        تحسن الأداء الأمني بنسبة 18% بعد تطبيق خوارزميات التعلم الجديدة
                    </div>
                </div>
            </div>
        </section>

        <!-- Reports Section -->
        <section id="reports" style="display: none;" class="dashboard">
            <div class="dashboard-card">
                <div class="card-header">
                    <div class="card-icon">
                        <i class="fas fa-file-alt"></i>
                    </div>
                    <div>
                        <h3 class="card-title">التقارير التشغيلية</h3>
                        <p>تقارير شاملة ومفصلة للأداء والمتابعة</p>
                    </div>
                </div>

                <div class="reports-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem; margin: 1rem 0;">
                    <div class="report-card" style="background: rgba(255, 255, 255, 0.1); border-radius: 10px; padding: 1.5rem; cursor: pointer;" onclick="generateReport('daily')">
                        <h4><i class="fas fa-calendar-day"></i> التقرير اليومي</h4>
                        <p>ملخص شامل لعمليات اليوم</p>
                        <small>آخر تحديث: اليوم 09:30 ص</small>
                    </div>
                    <div class="report-card" style="background: rgba(255, 255, 255, 0.1); border-radius: 10px; padding: 1.5rem; cursor: pointer;" onclick="generateReport('security')">
                        <h4><i class="fas fa-shield"></i> تقرير الأمن</h4>
                        <p>تحليل مفصل للوضع الأمني</p>
                        <small>آخر تحديث: أمس 11:45 م</small>
                    </div>
                    <div class="report-card" style="background: rgba(255, 255, 255, 0.1); border-radius: 10px; padding: 1.5rem; cursor: pointer;" onclick="generateReport('maintenance')">
                        <h4><i class="fas fa-wrench"></i> تقرير الصيانة</h4>
                        <p>حالة الطائرات والصيانة المطلوبة</p>
                        <small>آخر تحديث: اليوم 07:15 ص</small>
                    </div>
                    <div class="report-card" style="background: rgba(255, 255, 255, 0.1); border-radius: 10px; padding: 1.5rem; cursor: pointer;" onclick="generateReport('performance')">
                        <h4><i class="fas fa-chart-line"></i> تقرير الأداء</h4>
                        <p>مؤشرات الأداء الرئيسية والاتجاهات</p>
                        <small>آخر تحديث: اليوم 08:00 ص</small>
                    </div>
                </div>

                <div id="report-viewer" style="background: rgba(255, 255, 255, 0.05); border-radius: 15px; padding: 2rem; margin-top: 2rem; min-height: 300px;">
                    <h4>عارض التقارير</h4>
                    <p style="opacity: 0.7;">اختر أحد التقارير أعلاه لعرض التفاصيل</p>
                </div>
            </div>
        </section>
    </div>

    <!-- Modal -->
    <div id="modal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3 id="modal-title">عنوان النافذة</h3>
                <button class="close-modal" onclick="closeModal()">&times;</button>
            </div>
            <div id="modal-body">
                محتوى النافذة
            </div>
        </div>
    </div>

    <script>
        // Global Variables
        let charts = {};
        let scene, camera, renderer;
        let isTrainingActive = false;

        // Initialize the application
        window.addEventListener('DOMContentLoaded', function() {
            initializeCharts();
            initialize3D();
            startRealTimeUpdates();
            simulateAIProcessing();
        });

        // Navigation Functions
        function showSection(sectionName) {
            // Check if we are in airport dashboard mode
            const mainMap = document.getElementById('main-map');
            const airportDashboard = document.getElementById('airport-dashboard');
            
            if (airportDashboard.style.display !== 'none') {
                // We are in airport dashboard mode - show sections within airport dashboard
                showAirportSection(sectionName);
            } else {
                // We are in main map mode - hide main map and show full sections
                mainMap.style.display = 'none';
                
                // Hide all sections
                const sections = document.querySelectorAll('section');
                sections.forEach(section => section.style.display = 'none');
                
                // Show selected section
                const targetSection = document.getElementById(sectionName);
                if (targetSection) {
                    targetSection.style.display = 'block';
                } else {
                    document.getElementById('dashboard').style.display = 'block';
                }
            }
            
            // Update navigation
            document.querySelectorAll('.nav-item').forEach(item => {
                item.classList.remove('active');
            });
            
            // Find the clicked nav item and make it active
            const clickedItem = Array.from(document.querySelectorAll('.nav-item')).find(item => 
                item.getAttribute('onclick') && item.getAttribute('onclick').includes(sectionName)
            );
            if (clickedItem) {
                clickedItem.classList.add('active');
            }
        }

        function showAirportSection(sectionName) {
            // Hide other sections but keep airport dashboard visible
            const dashboardContainer = document.getElementById('airport-specific-dashboard');
            
            // Clear previous content
            dashboardContainer.innerHTML = '';
            
            // Get the section content and clone it
            const sourceSection = document.getElementById(sectionName);
            if (sourceSection) {
                const clonedContent = sourceSection.cloneNode(true);
                clonedContent.style.display = 'block';
                clonedContent.id = sectionName + '-airport-view';
                dashboardContainer.appendChild(clonedContent);
            }
        }

        // Initialize Charts
        function initializeCharts() {
            // Flight Traffic Chart
            const flightCtx = document.getElementById('flightChart').getContext('2d');
            charts.flight = new Chart(flightCtx, {
                type: 'line',
                data: {
                    labels: ['6:00', '8:00', '10:00', '12:00', '14:00', '16:00', '18:00'],
                    datasets: [{
                        label: 'عدد الرحلات',
                        data: [45, 89, 156, 234, 189, 167, 145],
                        borderColor: '#5D5CDE',
                        backgroundColor: 'rgba(93, 92, 222, 0.1)',
                        tension: 0.4,
                        fill: true
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            labels: { color: 'white' }
                        }
                    },
                    scales: {
                        x: { ticks: { color: 'white' } },
                        y: { ticks: { color: 'white' } }
                    }
                }
            });

            // Security Incidents Chart
            const securityCtx = document.getElementById('securityChart').getContext('2d');
            charts.security = new Chart(securityCtx, {
                type: 'doughnut',
                data: {
                    labels: ['آمن', 'تحت المراقبة', 'تهديد منخفض'],
                    datasets: [{
                        data: [85, 12, 3],
                        backgroundColor: ['#10b981', '#f59e0b', '#ef4444']
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            labels: { color: 'white' }
                        }
                    }
                }
            });

            // Maintenance Prediction Chart
            const maintenanceCtx = document.getElementById('maintenanceChart').getContext('2d');
            charts.maintenance = new Chart(maintenanceCtx, {
                type: 'bar',
                data: {
                    labels: ['الأسبوع 1', 'الأسبوع 2', 'الأسبوع 3', 'الأسبوع 4'],
                    datasets: [{
                        label: 'صيانة متوقعة',
                        data: [5, 8, 3, 12],
                        backgroundColor: '#fbbf24'
                    }, {
                        label: 'صيانة فعلية',
                        data: [3, 6, 2, 8],
                        backgroundColor: '#10b981'
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            labels: { color: 'white' }
                        }
                    },
                    scales: {
                        x: { ticks: { color: 'white' } },
                        y: { ticks: { color: 'white' } }
                    }
                }
            });

            // Weather Impact Chart
            const weatherCtx = document.getElementById('weatherChart').getContext('2d');
            charts.weather = new Chart(weatherCtx, {
                type: 'radar',
                data: {
                    labels: ['الرياح', 'الرطوبة', 'الرؤية', 'الحرارة', 'الضغط'],
                    datasets: [{
                        label: 'الوضع الحالي',
                        data: [3, 7, 9, 6, 8],
                        borderColor: '#0ea5e9',
                        backgroundColor: 'rgba(14, 165, 233, 0.2)'
                    }]
                },
                options: {
                    responsive: true,
                    scales: {
                        r: {
                            beginAtZero: true,
                            max: 10,
                            ticks: { color: 'white' },
                            grid: { color: 'rgba(255, 255, 255, 0.2)' }
                        }
                    },
                    plugins: {
                        legend: {
                            labels: { color: 'white' }
                        }
                    }
                }
            });

            // AI Performance Chart
            const aiCtx = document.getElementById('aiChart').getContext('2d');
            charts.ai = new Chart(aiCtx, {
                type: 'line',
                data: {
                    labels: ['يناير', 'فبراير', 'مارس', 'أبريل', 'مايو', 'يونيو'],
                    datasets: [{
                        label: 'دقة التنبؤ %',
                        data: [92, 94, 96, 98, 97, 99],
                        borderColor: '#7c3aed',
                        backgroundColor: 'rgba(124, 58, 237, 0.1)',
                        tension: 0.4,
                        fill: true
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            labels: { color: 'white' }
                        }
                    },
                    scales: {
                        x: { ticks: { color: 'white' } },
                        y: { 
                            ticks: { color: 'white' },
                            min: 90,
                            max: 100
                        }
                    }
                }
            });
        }

        // Initialize 3D Visualization
        function initialize3D() {
            const container = document.getElementById('threeCanvas');
            const width = container.parentElement.clientWidth;
            const height = 400;

            // Scene setup
            scene = new THREE.Scene();
            camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 1000);
            renderer = new THREE.WebGLRenderer({ canvas: container, antialias: true });
            renderer.setSize(width, height);
            renderer.setClearColor(0x1e3a8a);

            // Add lighting
            const ambientLight = new THREE.AmbientLight(0x404040, 0.6);
            scene.add(ambientLight);

            const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
            directionalLight.position.set(10, 10, 5);
            scene.add(directionalLight);

            // Create airport runway
            const runwayGeometry = new THREE.BoxGeometry(20, 0.1, 2);
            const runwayMaterial = new THREE.MeshLambertMaterial({ color: 0x333333 });
            const runway = new THREE.Mesh(runwayGeometry, runwayMaterial);
            scene.add(runway);

            // Create aircraft
            const aircraftGeometry = new THREE.ConeGeometry(0.5, 3, 8);
            const aircraftMaterial = new THREE.MeshLambertMaterial({ color: 0x5D5CDE });
            
            for (let i = 0; i < 5; i++) {
                const aircraft = new THREE.Mesh(aircraftGeometry, aircraftMaterial);
                aircraft.position.set(
                    (Math.random() - 0.5) * 15,
                    Math.random() * 2 + 1,
                    (Math.random() - 0.5) * 10
                );
                aircraft.rotation.y = Math.random() * Math.PI * 2;
                scene.add(aircraft);
            }

            // Create control tower
            const towerGeometry = new THREE.CylinderGeometry(1, 1, 8, 8);
            const towerMaterial = new THREE.MeshLambertMaterial({ color: 0xfbbf24 });
            const tower = new THREE.Mesh(towerGeometry, towerMaterial);
            tower.position.set(8, 4, 5);
            scene.add(tower);

            // Position camera
            camera.position.set(15, 10, 15);
            camera.lookAt(0, 0, 0);

            // Animation loop
            function animate() {
                requestAnimationFrame(animate);
                
                // Rotate the scene
                scene.rotation.y += 0.005;
                
                renderer.render(scene, camera);
            }
            animate();
        }

        // Real-time Data Updates
        function startRealTimeUpdates() {
            setInterval(() => {
                // Update flight count - only if element exists
                const flightCountElement = document.getElementById('flights-monitored');
                if (flightCountElement) {
                    const flightCount = 1200 + Math.floor(Math.random() * 100);
                    flightCountElement.textContent = flightCount.toLocaleString();
                }
                
                // Update active flights - only if element exists
                const activeFlightsElement = document.getElementById('active-flights');
                if (activeFlightsElement) {
                    const activeFlights = 300 + Math.floor(Math.random() * 100);
                    activeFlightsElement.textContent = activeFlights;
                }
                
                // Update passengers - only if element exists
                const passengersElement = document.getElementById('passengers-today');
                if (passengersElement) {
                    const passengers = 25000 + Math.floor(Math.random() * 5000);
                    passengersElement.textContent = passengers.toLocaleString();
                }
                
                // Update security alerts - only if element exists
                const alertsElement = document.getElementById('security-alerts');
                if (alertsElement) {
                    const alerts = Math.floor(Math.random() * 5);
                    alertsElement.textContent = alerts;
                }
                
                // Update response time - only if element exists
                const responseTimeElement = document.getElementById('response-time');
                if (responseTimeElement) {
                    const responseTime = 40 + Math.floor(Math.random() * 20);
                    responseTimeElement.textContent = responseTime;
                }
                
                // Update charts with new data
                updateChartsData();
            }, 3000);
        }

        function updateChartsData() {
            // Update flight chart
            if (charts.flight) {
                const newData = charts.flight.data.datasets[0].data.map(value => 
                    value + (Math.random() - 0.5) * 20
                );
                charts.flight.data.datasets[0].data = newData;
                charts.flight.update('none');
            }
        }

        // AI Processing Simulation
        function simulateAIProcessing() {
            const insights = [
                "تم كشف نمط غير عادي في حركة الركاب - يُنصح بالمراقبة الإضافية",
                "التنبؤ بزيادة الازدحام في البوابات 15-20 خلال الساعة القادمة",
                "مستوى الأمان مثالي - جميع الأنظمة تعمل بكفاءة عالية",
                "اكتشاف تحسن في أوقات الاستجابة بنسبة 15% هذا الأسبوع",
                "توصية بإجراء صيانة وقائية للطائرة SV-405 خلال 72 ساعة"
            ];
            
            setInterval(() => {
                const randomInsight = insights[Math.floor(Math.random() * insights.length)];
                showNotification("تحليل ذكي جديد", randomInsight, "info");
            }, 15000);
        }

        // Training Functions
        function startTraining(scenario) {
            isTrainingActive = true;
            let title, content;
            
            switch(scenario) {
                case 'fire':
                    title = "تدريب على مكافحة الحريق";
                    content = `
                        <div style="text-align: center;">
                            <i class="fas fa-fire" style="font-size: 3rem; color: #ef4444; margin-bottom: 1rem;"></i>
                            <h4>سيناريو حريق في الطائرة</h4>
                            <p>يتم الآن تحميل بيئة التدريب الافتراضية...</p>
                            <div class="loading" style="margin: 2rem auto;"></div>
                            <div style="background: rgba(239, 68, 68, 0.1); padding: 1rem; border-radius: 10px; margin-top: 1rem;">
                                <strong>إجراءات الطوارئ:</strong><br>
                                1. تنشيط إنذار الحريق<br>
                                2. إخلاء المنطقة المتضررة<br>
                                3. استخدام أجهزة الإطفاء المناسبة<br>
                                4. التواصل مع الفرق المختصة
                            </div>
                        </div>
                    `;
                    break;
                case 'security':
                    title = "تدريب التهديد الأمني";
                    content = `
                        <div style="text-align: center;">
                            <i class="fas fa-user-secret" style="font-size: 3rem; color: #ef4444; margin-bottom: 1rem;"></i>
                            <h4>سيناريو تهديد أمني</h4>
                            <p>تحميل محاكاة التعامل مع التهديدات الأمنية...</p>
                            <div class="loading" style="margin: 2rem auto;"></div>
                        </div>
                    `;
                    break;
                case 'medical':
                    title = "تدريب الطوارئ الطبية";
                    content = `
                        <div style="text-align: center;">
                            <i class="fas fa-heart" style="font-size: 3rem; color: #ef4444; margin-bottom: 1rem;"></i>
                            <h4>سيناريو طوارئ طبية</h4>
                            <p>تحميل بروتوكولات الإسعافات الأولية...</p>
                            <div class="loading" style="margin: 2rem auto;"></div>
                        </div>
                    `;
                    break;
                case 'evacuation':
                    title = "تدريب الإخلاء";
                    content = `
                        <div style="text-align: center;">
                            <i class="fas fa-running" style="font-size: 3rem; color: #f59e0b; margin-bottom: 1rem;"></i>
                            <h4>سيناريو إخلاء الطائرة</h4>
                            <p>تحميل إجراءات الإخلاء السريع...</p>
                            <div class="loading" style="margin: 2rem auto;"></div>
                        </div>
                    `;
                    break;
            }
            
            showModal(title, content);
            
            // Simulate training completion
            setTimeout(() => {
                closeModal();
                showNotification("تم إكمال التدريب", "تم إكمال السيناريو بنجاح! تم تسجيل النتائج.", "success");
                isTrainingActive = false;
            }, 5000);
        }

        // Emergency Response Functions
        function triggerEmergency(type) {
            let title, message, color;
            
            switch(type) {
                case 'fire':
                    title = "إنذار حريق";
                    message = "تم تفعيل إنذار الحريق في القطاع ج. الفرق في الطريق.";
                    color = "#ef4444";
                    break;
                case 'security':
                    title = "تهديد أمني";
                    message = "تم رصد تهديد أمني. تم تنبيه الفرق الأمنية.";
                    color = "#f59e0b";
                    break;
                case 'medical':
                    title = "طوارئ طبية";
                    message = "حالة طوارئ طبية في البوابة 8. تم استدعاء الإسعاف.";
                    color = "#ef4444";
                    break;
                case 'evacuation':
                    title = "إخلاء عام";
                    message = "تم تفعيل إجراءات الإخلاء العام. يرجى اتباع التعليمات.";
                    color = "#ef4444";
                    break;
            }
            
            showNotification(title, message, "emergency");
            
            // Simulate response tracking
            setTimeout(() => {
                showNotification("تحديث الحالة", "الفرق المختصة وصلت إلى الموقع.", "info");
            }, 3000);
            
            setTimeout(() => {
                showNotification("تم السيطرة", "تم التعامل مع الحالة بنجاح.", "success");
            }, 8000);
        }

        // Notification System
        function showNotification(title, message, type = 'info') {
            const notification = document.createElement('div');
            notification.className = 'notification';
            notification.style.cssText = `
                position: fixed;
                top: 100px;
                right: 20px;
                background: ${type === 'emergency' ? '#ef4444' : type === 'success' ? '#10b981' : '#5D5CDE'};
                color: white;
                padding: 1rem 1.5rem;
                border-radius: 10px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.3);
                z-index: 9999;
                max-width: 300px;
                animation: slideIn 0.3s ease;
                border-left: 5px solid rgba(255,255,255,0.5);
            `;
            
            notification.innerHTML = `
                <strong>${title}</strong><br>
                <small>${message}</small>
            `;
            
            document.body.appendChild(notification);
            
            setTimeout(() => {
                notification.style.animation = 'slideOut 0.3s ease';
                setTimeout(() => {
                    document.body.removeChild(notification);
                }, 300);
            }, 5000);
        }

        // Modal Functions
        function showModal(title, content) {
            document.getElementById('modal-title').textContent = title;
            document.getElementById('modal-body').innerHTML = content;
            document.getElementById('modal').style.display = 'block';
        }

        function closeModal() {
            document.getElementById('modal').style.display = 'none';
        }

        // Add CSS animations
        const style = document.createElement('style');
        style.textContent = `
            @keyframes slideIn {
                from { transform: translateX(100%); opacity: 0; }
                to { transform: translateX(0); opacity: 1; }
            }
            
            @keyframes slideOut {
                from { transform: translateX(0); opacity: 1; }
                to { transform: translateX(100%); opacity: 0; }
            }
            
            .notification {
                animation: slideIn 0.3s ease;
            }
        `;
        document.head.appendChild(style);

        // Performance monitoring
        function updatePerformanceMetrics() {
            const metrics = {
                responseTime: Math.random() * 100 + 20,
                accuracy: Math.random() * 5 + 95,
                uptime: Math.random() * 2 + 98,
                efficiency: Math.random() * 10 + 85
            };
            
            // Update metrics display if section is visible
            // This would be implemented based on current view
        }

        // Initialize performance monitoring
        setInterval(updatePerformanceMetrics, 5000);

        // Handle window resize for 3D canvas
        window.addEventListener('resize', () => {
            if (renderer && camera) {
                const container = document.getElementById('threeCanvas').parentElement;
                const width = container.clientWidth;
                const height = 400;
                
                camera.aspect = width / height;
                camera.updateProjectionMatrix();
                renderer.setSize(width, height);
            }
        });

        // Add keyboard shortcuts
        document.addEventListener('keydown', (e) => {
            if (e.altKey) {
                switch(e.key) {
                    case '1':
                        showSection('dashboard');
                        break;
                    case '2':
                        showSection('security');
                        break;
                    case '3':
                        showSection('safety');
                        break;
                    case '4':
                        showSection('analytics');
                        break;
                    case '5':
                        showSection('training');
                        break;
                }
            }
        });

        // Dark mode support
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            document.documentElement.classList.add('dark');
        }

        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', event => {
            if (event.matches) {
                document.documentElement.classList.add('dark');
            } else {
                document.documentElement.classList.remove('dark');
            }
        });

        // Add touch support for mobile
        let touchStartY = 0;
        document.addEventListener('touchstart', (e) => {
            touchStartY = e.touches[0].clientY;
        });

        document.addEventListener('touchmove', (e) => {
            const touchY = e.touches[0].clientY;
            const deltaY = touchStartY - touchY;
            
            // Smooth scrolling on mobile
            if (Math.abs(deltaY) > 50) {
                e.preventDefault();
            }
        });

        // Airport Data
        const airportsData = {
            riyadh: {
                name: "مطار الملك خالد الدولي",
                city: "الرياض",
                flights: 234,
                passengers: 12450,
                security: "آمن",
                weather: "مشمس 32°س",
                alerts: 0,
                aircraft: [
                    { id: "SV-101", status: "ممتاز", maintenance: "15 يوم" },
                    { id: "SV-202", status: "انتباه", maintenance: "48 ساعة" },
                    { id: "SV-303", status: "صيانة فورية", maintenance: "فوري" }
                ]
            },
            jeddah: {
                name: "مطار الملك عبدالعزيز الدولي",
                city: "جدة",
                flights: 189,
                passengers: 8950,
                security: "آمن",
                weather: "غائم 28°س",
                alerts: 1,
                aircraft: [
                    { id: "SV-401", status: "ممتاز", maintenance: "22 يوم" },
                    { id: "SV-402", status: "جيد", maintenance: "10 أيام" },
                    { id: "SV-403", status: "انتباه", maintenance: "72 ساعة" }
                ]
            },
            madinah: {
                name: "مطار الأمير محمد بن عبدالعزيز",
                city: "المدينة المنورة",
                flights: 98,
                passengers: 4120,
                security: "آمن",
                weather: "صحو 30°س",
                alerts: 0,
                aircraft: [
                    { id: "SV-301", status: "ممتاز", maintenance: "18 يوم" },
                    { id: "SV-302", status: "جيد", maintenance: "25 يوم" }
                ]
            },
            dammam: {
                name: "مطار الملك فهد الدولي",
                city: "الدمام",
                flights: 145,
                passengers: 6890,
                security: "تحت المراقبة",
                weather: "عاصفة رملية",
                alerts: 2,
                aircraft: [
                    { id: "SV-501", status: "جيد", maintenance: "8 أيام" },
                    { id: "SV-502", status: "انتباه", maintenance: "5 أيام" },
                    { id: "SV-503", status: "ممتاز", maintenance: "30 يوم" }
                ]
            }
        };

        // Airport Click Handler - Navigate to Airport Dashboard
        document.querySelectorAll('.airport-marker').forEach(marker => {
            marker.addEventListener('click', function() {
                const airport = this.getAttribute('data-airport');
                showAirportDashboard(airport);
            });
        });

        function showAirportDashboard(airportCode) {
            const airport = airportsData[airportCode];
            if (!airport) return;
            
            // Hide main map
            document.getElementById('main-map').style.display = 'none';
            
            // Show airport dashboard
            document.getElementById('airport-dashboard').style.display = 'block';
            
            // Update airport header
            const airportHeader = document.getElementById('airport-header');
            airportHeader.innerHTML = `
                <div class="airport-header-content">
                    <div style="display: flex; align-items: center; justify-content: center; gap: 1rem; margin-bottom: 2rem;">
                        <i class="fas fa-plane-departure" style="font-size: 3rem; color: #fbbf24;"></i>
                        <div style="text-align: center;">
                            <h1 class="airport-title">${airport.name}</h1>
                            <p class="airport-subtitle">${airport.city} - لوحة التحكم التشغيلية</p>
                        </div>
                    </div>
                    
                    <div class="airport-stats">
                        <div class="airport-stat">
                            <div class="airport-stat-number">${airport.flights}</div>
                            <div class="airport-stat-label">رحلات اليوم</div>
                        </div>
                        <div class="airport-stat">
                            <div class="airport-stat-number">${airport.passengers.toLocaleString()}</div>
                            <div class="airport-stat-label">مسافر</div>
                        </div>
                        <div class="airport-stat">
                            <div class="airport-stat-number" style="color: ${airport.security === 'آمن' ? '#10b981' : '#f59e0b'};">${airport.security}</div>
                            <div class="airport-stat-label">الوضع الأمني</div>
                        </div>
                        <div class="airport-stat">
                            <div class="airport-stat-number">${airport.weather}</div>
                            <div class="airport-stat-label">الأحوال الجوية</div>
                        </div>
                        <div class="airport-stat">
                            <div class="airport-stat-number">${airport.alerts}</div>
                            <div class="airport-stat-label">تنبيهات أمنية</div>
                        </div>
                    </div>
                </div>
            `;
            
            // Update data for the selected airport
            updateAirportData(airport);
            
            // Update navigation
            document.querySelectorAll('.nav-item').forEach(item => {
                item.classList.remove('active');
            });
            document.querySelector('.nav-item[onclick="showSection(\'dashboard\')"]').classList.add('active');
            
            // Show notification
            showNotification("تم التبديل للمطار", `تم عرض لوحة التحكم لـ ${airport.name}`, "success");
        }

        function showMainMap() {
            // Hide airport dashboard
            document.getElementById('airport-dashboard').style.display = 'none';
            
            // Show main map
            document.getElementById('main-map').style.display = 'block';
            
            // Update navigation
            document.querySelectorAll('.nav-item').forEach(item => {
                item.classList.remove('active');
            });
            
            // Show notification
            showNotification("العودة للخريطة", "تم العودة للخريطة الرئيسية", "info");
        }

        // Handle logo click to return to main map
        document.querySelector('.logo').addEventListener('click', function() {
            showMainMap();
        });

        function updateAirportData(airport) {
            // Update real-time data based on selected airport
            document.getElementById('active-flights').textContent = Math.floor(airport.flights * 0.3);
            document.getElementById('passengers-today').textContent = airport.passengers.toLocaleString();
            document.getElementById('security-alerts').textContent = airport.alerts;
            
            // Update aircraft status cards
            updateAircraftStatus(airport);
        }

        function updateAircraftStatus(airport) {
            const statusCards = document.querySelectorAll('.aircraft-status');
            if (statusCards.length >= 3) {
                airport.aircraft.forEach((aircraft, index) => {
                    if (statusCards[index]) {
                        const card = statusCards[index];
                        const statusClass = aircraft.status === 'ممتاز' ? '' : 
                                          aircraft.status === 'جيد' ? '' :
                                          aircraft.status === 'انتباه' ? 'warning' : 'critical';
                        
                        card.className = `aircraft-status ${statusClass}`;
                        card.innerHTML = `
                            <h4>${aircraft.id}</h4>
                            <p><strong>الحالة:</strong> ${aircraft.status} ${aircraft.status === 'ممتاز' ? '✅' : aircraft.status === 'جيد' ? '✅' : aircraft.status === 'انتباه' ? '⚠️' : '🔴'}</p>
                            <p><strong>الصيانة التالية:</strong> ${aircraft.maintenance}</p>
                            <p><strong>ساعات الطيران:</strong> ${Math.floor(Math.random() * 2000 + 500)} ساعة</p>
                        `;
                    }
                });
            }
        }

        function generateAirportReport(airportCode) {
            const airport = airportsData[airportCode];
            showNotification("جاري إنشاء التقرير", `يتم الآن إنشاء تقرير مفصل لـ ${airport.name}`, "info");
            
            setTimeout(() => {
                showNotification("تم إنشاء التقرير", "تم إنشاء التقرير بنجاح وإرساله للبريد الإلكتروني", "success");
                closeModal();
            }, 3000);
        }

        // Initialize additional charts for other sections
        function initializeAdditionalCharts() {
            // Security Analytics Chart
            setTimeout(() => {
                const securityAnalyticsCtx = document.getElementById('securityAnalyticsChart');
                if (securityAnalyticsCtx) {
                    charts.securityAnalytics = new Chart(securityAnalyticsCtx.getContext('2d'), {
                        type: 'line',
                        data: {
                            labels: ['الساعة 1', 'الساعة 2', 'الساعة 3', 'الساعة 4', 'الساعة 5', 'الساعة 6'],
                            datasets: [{
                                label: 'التهديدات المكتشفة',
                                data: [2, 1, 3, 0, 1, 2],
                                borderColor: '#ef4444',
                                backgroundColor: 'rgba(239, 68, 68, 0.1)',
                                tension: 0.4,
                                fill: true
                            }, {
                                label: 'الفحوصات المنجزة',
                                data: [45, 52, 48, 61, 55, 49],
                                borderColor: '#10b981',
                                backgroundColor: 'rgba(16, 185, 129, 0.1)',
                                tension: 0.4,
                                fill: true
                            }]
                        },
                        options: {
                            responsive: true,
                            plugins: {
                                legend: {
                                    labels: { color: 'white' }
                                }
                            },
                            scales: {
                                x: { ticks: { color: 'white' } },
                                y: { ticks: { color: 'white' } }
                            }
                        }
                    });
                }
            }, 1000);

            // Safety Chart
            setTimeout(() => {
                const safetyCtx = document.getElementById('safetyChart');
                if (safetyCtx) {
                    charts.safetyChart = new Chart(safetyCtx.getContext('2d'), {
                        type: 'bar',
                        data: {
                            labels: ['يناير', 'فبراير', 'مارس', 'أبريل', 'مايو', 'يونيو'],
                            datasets: [{
                                label: 'معدل السلامة %',
                                data: [98.5, 99.1, 98.9, 99.3, 99.7, 99.8],
                                backgroundColor: '#10b981'
                            }, {
                                label: 'الحوادث المنعة',
                                data: [15, 12, 18, 9, 6, 3],
                                backgroundColor: '#fbbf24'
                            }]
                        },
                        options: {
                            responsive: true,
                            plugins: {
                                legend: {
                                    labels: { color: 'white' }
                                }
                            },
                            scales: {
                                x: { ticks: { color: 'white' } },
                                y: { ticks: { color: 'white' } }
                            }
                        }
                    });
                }
            }, 1500);

            // Analytics Chart
            setTimeout(() => {
                const analyticsCtx = document.getElementById('analyticsChart');
                if (analyticsCtx) {
                    charts.analyticsChart = new Chart(analyticsCtx.getContext('2d'), {
                        type: 'doughnut',
                        data: {
                            labels: ['البيانات المعالجة', 'التحليلات المكتملة', 'التنبؤات النشطة', 'التقارير المنشئة'],
                            datasets: [{
                                data: [45, 30, 15, 10],
                                backgroundColor: ['#5D5CDE', '#10b981', '#fbbf24', '#ef4444']
                            }]
                        },
                        options: {
                            responsive: true,
                            plugins: {
                                legend: {
                                    labels: { color: 'white' }
                                }
                            }
                        }
                    });
                }
            }, 2000);
        }

        // Report Generation Functions
        function generateReport(type) {
            let title, content;
            
            switch(type) {
                case 'daily':
                    title = "التقرير اليومي";
                    content = `
                        <div style="background: rgba(255, 255, 255, 0.05); padding: 2rem; border-radius: 15px;">
                            <h4 style="color: #5D5CDE; margin-bottom: 2rem;">📊 ملخص العمليات اليومية</h4>
                            
                            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-bottom: 2rem;">
                                <div style="background: rgba(93, 92, 222, 0.1); padding: 1rem; border-radius: 8px;">
                                    <strong>إجمالي الرحلات:</strong> 666 رحلة
                                </div>
                                <div style="background: rgba(16, 185, 129, 0.1); padding: 1rem; border-radius: 8px;">
                                    <strong>إجمالي المسافرين:</strong> 32,457 مسافر
                                </div>
                                <div style="background: rgba(251, 191, 36, 0.1); padding: 1rem; border-radius: 8px;">
                                    <strong>معدل التأخير:</strong> 4.2%
                                </div>
                                <div style="background: rgba(239, 68, 68, 0.1); padding: 1rem; border-radius: 8px;">
                                    <strong>التنبيهات الأمنية:</strong> 3 تنبيهات
                                </div>
                            </div>
                            
                            <h5 style="margin: 1rem 0;">🏅 أفضل أداء:</h5>
                            <p>• مطار الملك خالد الدولي - 99.8% معدل الالتزام بالمواعيد</p>
                            <p>• مطار الملك عبدالعزيز الدولي - صفر حوادث أمنية</p>
                            
                            <h5 style="margin: 1rem 0;">⚠️ نقاط تحتاج انتباه:</h5>
                            <p>• زيادة الازدحام في مطار الدمام بسبب الطقس</p>
                            <p>• الحاجة لصيانة إضافية لطائرتين في جدة</p>
                        </div>
                    `;
                    break;
                    
                case 'security':
                    title = "تقرير الأمن";
                    content = `
                        <div style="background: rgba(255, 255, 255, 0.05); padding: 2rem; border-radius: 15px;">
                            <h4 style="color: #ef4444; margin-bottom: 2rem;">🛡️ تقرير الأمن الشامل</h4>
                            
                            <div style="background: rgba(16, 185, 129, 0.1); padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
                                <strong style="color: #10b981;">الوضع العام: آمن</strong>
                            </div>
                            
                            <h5 style="margin: 1rem 0;">📈 الإحصائيات:</h5>
                            <ul style="margin-left: 2rem;">
                                <li>15,432 مسافر تم فحصهم بنجاح</li>
                                <li>587 كاميرا مراقبة نشطة</li>
                                <li>99.7% معدل دقة الكشف</li>
                                <li>0.2% معدل الإنذارات الكاذبة</li>
                            </ul>
                            
                            <h5 style="margin: 1rem 0;">🚨 الأحداث المسجلة:</h5>
                            <p>• تم اكتشاف ومصادرة 3 عناصر محظورة</p>
                            <p>• 2 تنبيه أمني تم التعامل معه بنجاح</p>
                            <p>• تم توقيف شخص للاشتباه - تبين أنه سوء فهم</p>
                            
                            <h5 style="margin: 1rem 0;">💡 التوصيات:</h5>
                            <p>• زيادة الدوريات في مطار الدمام</p>
                            <p>• تحديث كاميرات المراقبة في القطاع ج</p>
                        </div>
                    `;
                    break;
                    
                case 'maintenance':
                    title = "تقرير الصيانة";
                    content = `
                        <div style="background: rgba(255, 255, 255, 0.05); padding: 2rem; border-radius: 15px;">
                            <h4 style="color: #fbbf24; margin-bottom: 2rem;">🔧 تقرير الصيانة التنبؤية</h4>
                            
                            <h5 style="margin: 1rem 0;">✅ الطائرات في حالة ممتازة:</h5>
                            <div style="background: rgba(16, 185, 129, 0.1); padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
                                <p>• SV-101, SV-301, SV-401, SV-503</p>
                                <p><strong>المجموع:</strong> 6 طائرات (60%)</p>
                            </div>
                            
                            <h5 style="margin: 1rem 0;">⚠️ طائرات تحتاج انتباه:</h5>
                            <div style="background: rgba(251, 191, 36, 0.1); padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
                                <p>• SV-202: مشكلة محتملة في المحرك</p>
                                <p>• SV-403: فحص دوري مطلوب</p>
                                <p>• SV-502: تآكل طفيف في الأجنحة</p>
                            </div>
                            
                            <h5 style="margin: 1rem 0;">🔴 صيانة فورية:</h5>
                            <div style="background: rgba(239, 68, 68, 0.1); padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
                                <p>• SV-303: مشكلة في النظام الهيدروليكي</p>
                                <p><strong>الإجراء:</strong> توقف فوري تم تنفيذه</p>
                            </div>
                            
                            <h5 style="margin: 1rem 0;">📊 إحصائيات الأداء:</h5>
                            <p>• 96% من الأعطال تم توقعها مسبقاً</p>
                            <p>• انخفاض زمن الصيانة إلى 4.2 ساعة</p>
                            <p>• 87% تغطية بالصيانة التنبؤية</p>
                        </div>
                    `;
                    break;
                    
                case 'performance':
                    title = "تقرير الأداء";
                    content = `
                        <div style="background: rgba(255, 255, 255, 0.05); padding: 2rem; border-radius: 15px;">
                            <h4 style="color: #10b981; margin-bottom: 2rem;">📈 تقرير مؤشرات الأداء</h4>
                            
                            <h5 style="margin: 1rem 0;">🎯 المؤشرات الرئيسية:</h5>
                            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-bottom: 2rem;">
                                <div style="background: rgba(93, 92, 222, 0.1); padding: 1rem; border-radius: 8px; text-align: center;">
                                    <div style="font-size: 1.8rem; font-weight: bold; color: #5D5CDE;">99.8%</div>
                                    <div>معدل كشف التهديدات</div>
                                </div>
                                <div style="background: rgba(16, 185, 129, 0.1); padding: 1rem; border-radius: 8px; text-align: center;">
                                    <div style="font-size: 1.8rem; font-weight: bold; color: #10b981;">45s</div>
                                    <div>متوسط زمن الاستجابة</div>
                                </div>
                                <div style="background: rgba(251, 191, 36, 0.1); padding: 1rem; border-radius: 8px; text-align: center;">
                                    <div style="font-size: 1.8rem; font-weight: bold; color: #fbbf24;">98.7%</div>
                                    <div>دقة التنبؤات</div>
                                </div>
                                <div style="background: rgba(239, 68, 68, 0.1); padding: 1rem; border-radius: 8px; text-align: center;">
                                    <div style="font-size: 1.8rem; font-weight: bold; color: #ef4444;">0.01</div>
                                    <div>حوادث/مليون رحلة</div>
                                </div>
                            </div>
                            
                            <h5 style="margin: 1rem 0;">📊 الاتجاهات:</h5>
                            <p>• تحسن الأداء الأمني بنسبة 18% هذا الشهر</p>
                            <p>• انخفاض معدل التأخير بنسبة 23%</p>
                            <p>• زيادة رضا المسافرين إلى 96.5%</p>
                            
                            <h5 style="margin: 1rem 0;">🏆 الإنجازات:</h5>
                            <p>• تم منع 45 حادثة محتملة هذا الشهر</p>
                            <p>• تدريب 847 موظف على الأنظمة الجديدة</p>
                            <p>• تطبيق 156 نموذج ذكي للتحليل</p>
                        </div>
                    `;
                    break;
            }
            
            document.getElementById('report-viewer').innerHTML = content;
            showNotification("تم تحديث التقرير", `تم عرض ${title} بنجاح`, "success");
        }

        // Call additional initialization
        setTimeout(() => {
            initializeAdditionalCharts();
        }, 2000);

        console.log('🦅 عين الصقر - منظومة سلامة وأمن الطيران الذكية تم تحميلها بنجاح');
        console.log('📊 جميع الأنظمة تعمل بكفاءة عالية');
        console.log('🛡️ الحماية الأمنية مفعلة');
        console.log('🗺️ الخريطة التفاعلية جاهزة');
        console.log('🚀 جاهز للعمل!');
    </script>
</body>
</html>
