# A3
<p align="center">
    <img src="https://github.com/wakaDnna/A3/assets/147518230/f2d04341-0199-4be1-80c0-d690543a84d0"/>
</p>

# 開発環境
Python 3.11.5

# ER Diagram

```mermaid

erDiagram
    users{
        int id PK
        string(50) name
        string(50) display_id 
        int followers_count
        int following_count
        date birthday
        text bio
        mediumblob image
    }

```