# スケジュール通知BOT
毎日の講義連絡をLINEでお知らせしてくれるBOTです

[詳細説明](https://www.resume.id/works/2159b750fa1b163f)

# 作ったきっかけ
授業が休校だと気づかずに１時間半かけて通学したにも関わらず、教室には誰もいなかったという経験が何度かあった。

## 大学公式iOSアプリの問題点
- 大学のアプリでは休校通知がこない。
- 自分でスケジュールを確認しないといけない。
- 毎回アプリにログインするのが面倒臭く、使い勝手が悪すぎる。
- 最後にアップデートされたのが2年前で、おそらく保守されていない。
- UIが古いため使いづらい

# キャプチャ
<img src="images/IMG_0855.PNG" width="300px">

# 設計
1. seleniumで大学の自分のアカウントのサイトにログイン
2. 本日の時間割をスクレイピングする
3. 抽出した内容をLINE Messaging API でプッシュ通知

これらの作業を毎朝決まった時間に行う
