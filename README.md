## デモを動かすまで

### セットアップ

```bash
git clone https://github.com/sharp0416/axbench.git
cd axbench
uv sync
```

### ローカルLLMサーバーを立てる

```bash
cd your_server_dir
bash serve_your_llm.sh # e.g. base_url==http://127.0.0.1:8000/v1
```

### 環境変数の設定

```bash
export HF_TOKEN=hf_xxxxxxxxxxxxxxxxx
export BASE_URL=your_base_model_url # e.g. http://127.0.0.1:8000/v1
```

### `axbench/data`にデータをダウンロード:

```bash
uv run axbench/data/download-seed-sentences.py
cd axbench/data
bash download-2b.sh
bash download-9b.sh
bash download-alpaca.sh
```

### デモ動作

```bash
bash axbench/demo/demo.sh
```

## 注意事項

### ローカルモデルの変更について

`axbench/demo/sweep/simple`でデフォルト`Qwen/Qwen3-VL-8B-Instruct`と示している部分を変更せよ

### デモ実行中のスタックについて

デモ動作中、スタックすることがある。目安として、GPU計算率が100%に張り付き、ログが更新されないという兆候がでたらその状況なので、その場合はctrl+Cでプロセスを終了させる。上記のスクリプトはスタックした部分から再開してくれるようなので、問題ないはず。