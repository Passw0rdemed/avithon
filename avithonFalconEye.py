
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
        <!-- Hero Section -->
        <section class="hero">
            <div class="hero-content">
                <h1>عين الصقر</h1>
                <p>منظومة ذكية متكاملة لتعزيز أمن وسلامة قطاع الطيران باستخدام الذكاء الاصطناعي والتقنيات المتقدمة</p>
                
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-number" id="airports-count">27</div>
                        <div class="stat-label">مطار محمي</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number" id="flights-monitored">1,247</div>
                        <div class="stat-label">رحلة مراقبة يومياً</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number" id="threats-prevented">99.8%</div>
                        <div class="stat-label">معدل كشف التهديدات</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number" id="response-time">45</div>
                        <div class="stat-label">ثانية متوسط الاستجابة</div>
                    </div>
                </div>
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

        <!-- Emergency Response -->
        <section id="emergency" style="display: none;">
            <div class="dashboard-card">
                <div class="card-header">
                    <div class="card-icon">
                        <i class="fas fa-exclamation-triangle"></i>
                    </div>
                    <div>
                        <h3 class="card-title">نظام الاستجابة للطوارئ</h3>
                        <p>استجابة سريعة ومنسقة للحالات الطارئة</p>
                    </div>
                </div>

                <div class="emergency-panel">
                    <h4>إجراءات الطوارئ</h4>
                    <div class="emergency-actions">
                        <div class="action-button" onclick="triggerEmergency('fire')">
                            <i class="fas fa-fire"></i>
                            <div>إنذار حريق</div>
                        </div>
                        <div class="action-button" onclick="triggerEmergency('security')">
                            <i class="fas fa-shield-alt"></i>
                            <div>تهديد أمني</div>
                        </div>
                        <div class="action-button" onclick="triggerEmergency('medical')">
                            <i class="fas fa-ambulance"></i>
                            <div>طوارئ طبية</div>
                        </div>
                        <div class="action-button" onclick="triggerEmergency('evacuation')">
                            <i class="fas fa-running"></i>
                            <div>إخلاء عام</div>
                        </div>
                    </div>
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
            
            // Update navigation
            document.querySelectorAll('.nav-item').forEach(item => {
                item.classList.remove('active');
            });
            event.target.classList.add('active');
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
                // Update flight count
                const flightCount = 1200 + Math.floor(Math.random() * 100);
                document.getElementById('flights-monitored').textContent = flightCount.toLocaleString();
                
                // Update active flights
                const activeFlights = 300 + Math.floor(Math.random() * 100);
                document.getElementById('active-flights').textContent = activeFlights;
                
                // Update passengers
                const passengers = 25000 + Math.floor(Math.random() * 5000);
                document.getElementById('passengers-today').textContent = passengers.toLocaleString();
                
                // Update security alerts
                const alerts = Math.floor(Math.random() * 5);
                document.getElementById('security-alerts').textContent = alerts;
                
                // Update response time
                const responseTime = 40 + Math.floor(Math.random() * 20);
                document.getElementById('response-time').textContent = responseTime;
                
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

        console.log('🦅 عين الصقر - منظومة سلامة وأمن الطيران الذكية تم تحميلها بنجاح');
        console.log('📊 جميع الأنظمة تعمل بكفاءة عالية');
        console.log('🛡️ الحماية الأمنية مفعلة');
        console.log('🚀 جاهز للعمل!');
    </script>
</body>
</html>


