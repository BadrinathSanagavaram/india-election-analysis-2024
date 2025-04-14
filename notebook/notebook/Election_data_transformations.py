import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
import datetime
import plotly.express as px
import plotly.graph_objects as go

# Reading the Data
df = pd.read_csv('/Users/badrinathsanagavaram/Desktop/GitHUB practice folder/Python Pandas Projects/india-election-analysis-2024/data/elections-data-2024-cleaned.csv')
df["Constituency"] = df["Constituency"].str.replace(r'\s*\([^)]*\)', '', regex=True)
df
df[df['Constituency'].duplicated()]
df[df["Constituency"] == 'araku'] # checking for duplicates in the constituency column
df.sort_values(by = 'Constituency' ,ascending=True, inplace=True) # sorting the dataframe by constituency
df.head(50)
df.columns

lok_sabha_constituencies = {
    'Andhra Pradesh': [
        'amalapuram', 'anakapalle', 'araku', 'bapatla', 'chittoor', 'eluru',
        'guntur', 'hindupur', 'kadapa', 'kakinada', 'kurnoolu', 'machilipatnam',
        'nandyal', 'narasapuram', 'narsaraopet', 'nellore', 'ongole',
        'rajahmundry', 'rajampet', 'srikakulam', 'thirupathi', 'vijayawada',
        'visakhapatnam', 'vizianagaram'
    ],
    'Arunachal Pradesh': [
        'arunachal east', 'arunachal west'
    ],
    'Assam': [
        'darrang-udalguri', 'dibrugarh', 'diphu', 'guwahati', 'jorhat',
        'karimganj', 'kaziranga', 'kokrajhar', 'nagaon', 'silchar', 'sonitpur'
    ],
    'Bihar': [
        'araria', 'arrah', 'aurangabad', 'banka', 'begusarai', 'buxar',
        'darbhanga', 'gaya', 'jahanabad', 'jamui', 'jhanjharpur', 'karakat',
        'katihar', 'khagaria', 'kishanganj', 'madhepura', 'madhubani',
        'maharajganj', 'munger', 'muzaffarpur', 'nalanda', 'nawada',
        'paschim champaran', 'patliputra', 'patna sahib', 'purnia',
        'purvi champaran', 'samastipur', 'saran', 'sasaram', 'sheohar',
        'sitamarhi', 'supaul', 'ujiyarpur', 'valmiki nagar', 'vaishali'
    ],
    'Chhattisgarh': [
        'balod', 'bilaspur', 'durg', 'janjgir-champa', 'korba', 'raigarh',
        'raipur', 'rajnandgaon', 'surguja'
    ],
    'Goa': [
        'north goa', 'south goa'
    ],
    'Gujarat': [
        'ahmedabad east', 'ahmedabad west', 'amreli', 'anand', 'banaskantha',
        'bardoli', 'bharuch', 'bhavnagar', 'chhota udaipur', 'dahod',
        'gandhinagar', 'jamnagar', 'junagadh', 'kachchh', 'kheda', 'mahesana',
        'navsari', 'panchmahal', 'patan', 'porbandar', 'rajkot', 'sabarkantha',
        'surat', 'surendranagar', 'vadodara', 'valsad'
    ],
    'Haryana': [
        'ambala', 'bhiwani-mahendragarh', 'faridabad', 'fatehabad', 'gurgaon',
        'hisar', 'karnal', 'kurukshetra', 'rohtak', 'sirsa', 'sonipat'
    ],
    'Himachal Pradesh': [
        'hamirpur', 'kangra', 'mandi', 'shimla'
    ],
    'Jharkhand': [
        'chatra', 'dhanbad', 'dumka', 'giridih', 'godda', 'hazaribagh',
        'jamshedpur', 'khunti', 'kodarma', 'lohardaga', 'palamau', 'rajmahal',
        'ranchi', 'singhbhum'
    ],
    'Karnataka': [
        'bagalkot', 'bangalore central', 'bangalore north', 'bangalore rural',
        'bangalore south', 'belgaum', 'bellary', 'bidar', 'bijapur', 'chamarajanagar',
        'chikkballapur', 'chikkodi', 'chitradurga', 'davanagere', 'dharwad',
        'gulbarga', 'hassan', 'haveri', 'kolar', 'koppal', 'mandya', 'mysore',
        'raichur', 'shimoga', 'tumkur', 'udupi chikmagalur', 'uttara kannada'
    ],
    'Kerala': [
        'alappuzha', 'alathur', 'attingal', 'chalakudy', 'ernakulam', 'idukki',
        'kannur', 'kasaragod', 'kollam', 'kottayam', 'kozhikode', 'malappuram',
        'mavelikkara', 'palakkad', 'pathanamthitta', 'ponnani', 'thrissur',
        'vadakara', 'wayanad'
    ],
    'Madhya Pradesh': [
        'balaghat', 'betul', 'bhind', 'bhopal', 'chhindwara', 'damoh', 'dewas',
        'dhar', 'guna', 'gwalior', 'hoshangabad', 'indore', 'jabalpur',
        'khajuraho', 'khandwa', 'khargone', 'mandsour', 'morena', 'raisen',
        'ratlam', 'rewa', 'sagar', 'satna', 'shahdol', 'sidhi', 'tikamgarh',
        'ujjain', 'vidisha'
    ],
    'Maharashtra': [
        'ahmednagar', 'akola', 'amravati', 'aurangabad', 'baramati', 'beed',
        'bhandara gondiya', 'bhiwandi', 'buldhana', 'chandrapur', 'dhule',
        'gadchiroli - chimur', 'hatkanangale', 'hingoli', 'jalgaon', 'jalna',
        'kolhapur', 'latur', 'maval', 'mumbai north', 'mumbai north central',
        'mumbai north east', 'mumbai north west', 'mumbai south',
        'mumbai south central', 'nanded', 'nandurbar', 'nashik', 'osmanabad',
        'palghar', 'parbhani', 'pune', 'raigad', 'ramtek', 'ratnagiri- sindhudurg',
        'raver', 'satara', 'shirdi', 'shirur', 'solapur', 'thane', 'wardha',
        'yavatmal- washim'
    ],
    'Manipur': [
        'inner manipur', 'outer manipur'
    ],
    'Meghalaya': [
        'Shillong', 'Tura'
    ],
    'Mizoram': [
        'mizoram'
    ],
    'Nagaland': [
        'nagaland'
    ],
    'Odisha': [
        'asika', 'balangir', 'bargarh', 'berhampur', 'bhadrak', 'cuttack', 'dhenkanal',
        'jagatsinghpur', 'jajpur', 'kendrapara', 'keonjhar', 'koraput', 'kalahandi', 'mayurbhanj',
        'nabarangpur', 'puri', 'sambalpur', 'sundargarh'
    ],
    'Punjab': [
        'amritsar', 'anandpur sahib', 'bathinda', 'fatehgarh sahib', 'faridkot', 'firozpur',
        'gurdaspur', 'hoshiarpur', 'jalandhar', 'khadoor sahib', 'ludhiana', 'patiala', 'sangrur'
    ],
    'Rajasthan': [
        'ajmer', 'alwar', 'barmer', 'bharatpur', 'bhilwara', 'bikaner', 'chittorgarh', 'churu',
        'dausa', 'dholpur-karauli', 'jaipur', 'jaipur rural', 'jhalawar-baran', 'jhunjhunu', 'jodhpur',
        'kota', 'nagaur', 'rajsamand', 'sikar', 'tonk-sawai madhopur', 'udaipur'
    ],
    'Sikkim': [
        'sikkim'
    ],
    'Tamil Nadu': [
        'chennai central', 'chennai north', 'chennai south', 'coimbatore', 'cuddalore', 'dharmapuri',
        'erode', 'karur', 'kallakurichi', 'kancheepuram', 'krishnagiri', 'madurai', 'mayiladuthurai',
        'nagapattinam', 'namakkal', 'nilgiris', 'perambalur', 'pollachi', 'ponnani', 'ramanathapuram',
        'salem', 'sivaganga', 'sriperumbudur', 'tenkasi', 'thanjavur', 'theni', 'thiruvallur',
        'thiruvananthapuram', 'thoothukkudi', 'tiruchirappalli', 'tirunelveli', 'tiruppur',
        'tiruvannamalai', 'viluppuram', 'virudhunagar'
    ],
    'Telangana': [
        'adilabad', 'bhongir', 'chevella', 'khammam', 'mahabubabad', 'mahbubnagar', 'medak',
        'malkajgiri', 'nagarkurnool', 'nalgonda', 'nizamabad', 'peddapalle', 'secunderabad', 'warangal',
        'zahirabad', 'hyderabad'
    ],
    'Tripura': [
        'tripura west', 'tripura east'
    ],
    'Uttar Pradesh': [
        'agra', 'akhbarpur', 'amethi', 'amroha', 'aonla', 'azamgarh', 'badaun', 'baghpat',
        'baharaich', 'ballia', 'banda', 'barabanki', 'bareilly', 'basti', 'bhadohi', 'bijnor',
        'bulandshahr', 'chandauli', 'domariyaganj', 'etah', 'etawah', 'faizabad', 'farrukhabad',
        'fatehpur', 'fatehpur sikri', 'firozabad', 'gautam buddha nagar', 'ghaziabad', 'ghazipur',
        'ghosi', 'gonda', 'gorakhpur', 'hamirpur', 'hardoi', 'hathras', 'jaunpur', 'jhansi',
        'kairana', 'kaiserganj', 'kanpur', 'kaushambi', 'kheri', 'kushi nagar', 'lalganj', 'lucknow',
        'machhlishahr', 'mainpuri', 'mathura', 'meerut', 'misrikh', 'mohanlalganj', 'moradabad',
        'muktsar', 'muzaffarnagar', 'nagina', 'phulpur', 'pilibhit', 'pratapgarh', 'rae bareli',
        'rampur', 'robertsganj', 'saharanpur', 'salempur', 'sambhal', 'sant kabir nagar', 'shrawasti',
        'siddharthnagar', 'sitapur', 'sultanpur', 'unnao', 'varanasi'
    ],
    'Uttarakhand': [
        'garhwal', 'hardwar', 'nainital-udhamsingh nagar', 'tehri garhwal', 'almora'
    ],
    'West Bengal': [
        'alipurduars', 'arambagh', 'bangaon', 'bankura', 'barasat', 'bardhaman purba', 'bardhaman-durgapur',
        'basirhat', 'birbhum', 'bishnupur', 'coochbehar', 'diamond harbour', 'dum dum', 'ghatal',
        'hooghly', 'howrah', 'jalpaiguri', 'jhargram', 'joynagar', 'krishnanagar', 'malda dakshin',
        'malda uttar', 'medinipur', 'murshidabad', 'raiganj', 'ranaghat', 'srerampur', 'srirampur',
        'tamralipta', 'tamluk', 'uluberia'
    ],
    'Andaman & Nicobar Islands': ['andaman & nicobar islands'],
    'Chandigarh': ['chandigarh'],
    'Dadra and Nagar Haveli and Daman and Diu': ['dadar & nagar haveli', 'daman & diu'],
    'Delhi': [
        'chandni chowk', 'east delhi', 'new delhi', 'north-east delhi', 'north-west delhi',
        'south delhi', 'west delhi'
    ],
    'Jammu and Kashmir': [
        'anantnag-rajouri', 'baramulla', 'jammu', 'srinagar', 'udhampur'
    ],
    'Ladakh': ['ladakh'],
    'Lakshadweep': ['lakshadweep'],
    'Puducherry': ['puducherry']
}

state_cons = {"state":[],
              "Constituency": []}

for key , val in lok_sabha_constituencies.items():
    for i in range (0,len(val)):
        state_cons["state"].append(key)
        state_cons["Constituency"].append(val[i])
state_cons
state_wise_constituencies = pd.DataFrame(state_cons)
state_wise_constituencies

df_merge = pd.merge(df, state_wise_constituencies, on='Constituency', how='inner')
df_merge.shape
df_merge.isna().sum()

Rahul_gandhi_vs_narendra_modi = df_merge[['Leading Candidate', 'Constituency', 'Margin']][df_merge['Leading Candidate'] == "RAHUL GANDHI"]
Rahul_gandhi_vs_narendra_modi.plot(kind='bar', title="Rahul Gandhi Performace", xlabel="Margin", ylabel='Constituency')
plt.show()

df_merge.to_csv("/Users/badrinathsanagavaram/Desktop/GitHUB practice folder/Python Pandas Projects/india-election-analysis-2024/data/elections-data-2024-cleaned.csv", index=False)