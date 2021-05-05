import streamlit as st
import numpy as np
import pandas as pd
import time
st.title('streamlit  超入門')

st.write('progressbar')
# st.write('Interactive Widgets')
'Start!!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i + 1}')
    bar.progress(i + 1)
    time.sleep(0.01)

'Done!!!'



left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここに右カラム')

expander1 = st.beta_expander('問合せ１')
expander1.write('問合せ１の回答')
expander2 = st.beta_expander('問合せ2')
expander2.write('問合せ2の回答')
expander3 = st.beta_expander('問合せ3')
expander3.write('問合せ3の回答')



# st.write('DataFrame')
# text = st.text_input('plese tell me your favrito hobby')

# 'your hobby is',text
# st.sideber.write  => sider
# condition = st.sidebar.slider('how are you?',0,100,50)
# 'your condition',condition

# option = st.selectbox(
#     'あなたの好きな数字を教えてください',
#     list(range(1, 11))
# )
# 'あなたの好きな数字は',option,'です'
# df = pd.DataFrame(
    # '1列目':[1, 2, 3, 4],   
    # '2列目':[10, 20, 30, 40]   
#     np.random.rand(100,2)/[50, 50]+[35.69, 139.70],
#     columns=['lat','lon']

# )

# st.map(df)
# st.line_chart(df)
# st.area_chart(df)


# st.table(df.style.highlight_max(axis=0))



# """
#     python

#     import streamlit as st
#     import numpy as np
#     import pandas as pd

# """