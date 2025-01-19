# backend/utils/constants.py
BASE_URL = 'http://localhost:5000'

KEYWORDS = {
    'skripsi': 'jadwal_ta',
    'ta': 'jadwal_ta',
    'tugas akhir': 'jadwal_ta',
    'kerja praktek': 'jadwal_kp',
    'kp': 'jadwal_kp',
    'magang': 'jadwal_kp',
    'kuliah': 'jadwal_kuliah',
    'kelas': 'jadwal_kuliah'
}

RESPONSES = {
    'jadwal_kuliah': {
        'text': 'Woww, tumben rajin banget sampai nanyain jadwal kelas🤩. Okayy, jadwalnya aku lampirin digambar ini yaa. Jangan lupa sarapan kalau masuk pagi dan libur waktunya healing~ ✨',
        'image': {
            'type': 'image',
            'url': f'{BASE_URL}/static/images/jadwal_kelas.jpg',
            'alt': 'Jadwal Kuliah',
            'caption': 'Timeline Kuliah'
        }
    },
    'jadwal_kp': {
        'text': 'Inii jadwal prakteknyaa. Tetap semangat yaa, jangan lupa minum vitamin biar ga drop badan kamu💪🏼😁',
        'image': {
            'type': 'image',
            'url': f'{BASE_URL}/static/images/jadwal_kp.jpg',
            'alt': 'Jadwal KP',
            'caption': 'Timeline Kerja Praktek'
        }
    },
    'jadwal_ta': {
        'text': 'Hayoo jangan kebanyakan rebahan sambil scroll tiktok, katanya mau cepat lulus😩, semangat kerjain Tugas Akhirnya💪🏼😁. ',
        'image': {
            'type': 'image',
            'url': f'{BASE_URL}/static/images/jadwal_ta.jpg',
            'alt': 'Jadwal TA',
            'caption': 'Timeline Tugas Akhir'
        }
    }   
}
