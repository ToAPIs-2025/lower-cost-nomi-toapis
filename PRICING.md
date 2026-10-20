# Case amounts and model rates / 本例花费与模型价格

2026-10-20.

| Model / preset | Type | Case amount / quote | Applicable model rate | Fee evidence |
|---|---|---:|---|---|
| gpt-image-2(VIP)<br>low / 1K | image | Quoted $0.0019 | $0.0019/image | Configured rate; task billing unavailable |
| gpt-image-2<br>1K | image | Quoted $0.015 | $0.015/image | Configured rate; task billing unavailable |
| gpt-image-2.5-flare<br>high / 1K | image | Quoted $0.0225 | $0.0225/image | Configured rate; task billing unavailable |
| seedance-2-mini<br>480p / 4.04s / no audio | video | $0.13338 | $3.285714/1M total tokens | API billing=settled |

| 模型／档位 | 类型 | 本例金额／报价 | 对应模型价格 | 费用依据 |
|---|---|---:|---|---|
| gpt-image-2(VIP)<br>low / 1K | 图片 | 报价 $0.0019 | $0.0019/image | 档位报价；单任务未返回结算 |
| gpt-image-2<br>1K | 图片 | 报价 $0.015 | $0.015/image | 档位报价；单任务未返回结算 |
| gpt-image-2.5-flare<br>high / 1K | 图片 | 报价 $0.0225 | $0.0225/image | 档位报价；单任务未返回结算 |
| seedance-2-mini<br>480p / 4.04s / 无声 | 视频 | $0.13338 | $3.285714/1M total tokens | API billing=settled |

[Current-key pricing documentation](https://docs.toapis.com/docs/en/api-reference/account/pricing). Rates are not a reserved generation quote. Receipt settlement takes priority; raw account logs and credentials are private.

<!-- extra-video-models -->

## Additional video cases, ascending

| Model | Request | Decoded length | API-settled cost | Case USD/s | Current preset rate |
|---|---|---:|---:|---:|---|
| kling-3.0-turbo | 4s / 720p | 4.04s | $0.32 | $0.079208/s | $0.08/s |
| MiniMax-H3 | 5s / 768p | 5.17s | $0.32 | $0.061896/s | $0.064/s |
| seedance-2-5 | 4s / 480p | 4.04s | $0.3883 | $0.096114/s | $10/1M total tokens |

Independent T2V calls, different resolution/duration. [Full evidence](video-comparison/README.md).
