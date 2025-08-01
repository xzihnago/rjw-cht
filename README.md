# RJW 中文化

RJW 與部分附加模組的中文化。<br />
目標是提供 RJW 與附加模組之間翻譯風格的一致性，以及與官方社群繁體中文用詞盡可能貼近的翻譯。

### 維護中的模組

可能有翻譯錯誤、詞不達意或用詞不一致的情況，若有問題還請提出。

| 模組                                                                                                | 版本     | 狀態                         |
| --------------------------------------------------------------------------------------------------- | -------- | ---------------------------- |
| [RimJobWorld](https://gitgud.io/Ed86/rjw)                                                           | `5c23d8` | 完整                         |
| [RimJobWorld - Cum](https://gitgud.io/Ed86/rjw-cum)                                                 | `21af8a` | 完整                         |
| [RimJobWorld - FB](https://gitgud.io/Ed86/rjw-fb)                                                   | `9080ca` | 完整                         |
| [RimJobWorld - FC](https://gitgud.io/Ed86/rjw-fc)                                                   | `dca868` | 完整                         |
| [RimJobWorld - FH](https://gitgud.io/Ed86/rjw-fh)                                                   | `be266b` | 完整                         |
| [RimJobWorld - STD](https://gitgud.io/Nalzurin/rjw-std)                                             | `0cfa87` | 完整                         |
| [RJW Sexperience](https://gitgud.io/amevarashi/rjw-sexperience)                                     | `f86a54` | 完整                         |
| [RJW Sexperience Ideology](https://gitgud.io/amevarashi/rjw-sexperience-ideology)                   | `0294af` | 完整                         |
| [RJW Menstruation Cycle](https://gitgud.io/lutepickle/rjw_menstruation)                             | `ac1a64` | 完整                         |
| [RJW Menstruation - Resources](https://gitgud.io/ElToro/rjw-menstruation-resources)                 | `4c915b` | 完整                         |
| [Cumpilation](https://github.com/vegapnk/Cumpilation)                                               | `b6439b` | 完整                         |
| [RimJobWorld - Licentia Labs Stretching Edition](https://gitgud.io/ElToro/licentia-labs-stretching) | `488fed` | 完整                         |
| [RJW Race Support](https://gitgud.io/WinterKein/rjw-race-support)                                   | `b6c1fa` | 完整（部分跨模組支援未翻譯） |
| [RJW Genes](https://github.com/vegapnk/RJW-Genes)                                                   | `7540b9` | 完整（部分跨模組支援未翻譯） |
| [Fantasy Races](https://gitgud.io/Euclidean/Fantasy-Races)                                          | `f29fca` | 完整                         |
| [RimJobWorld - Extension](https://gitgud.io/Nalzurin/rjw-extension)                                 | `ff57f5` | 完整                         |
| [Sized Apparel for RJW (SAR version)](https://gitgud.io/jikulopo/sized-apparel-zero)                | `a902ee` | 補全（紋身）                 |
| [Sized Apparel for Slaves](https://gitgud.io/cptyossarian/sized-apparel-for-slaves)                 | `01a47f` | 完整                         |
| [Rimworld Animations 2.0](https://gitgud.io/c0ffeeeeeeee/rimworld-animations)                       | `e96305` | 補全（選單按鈕）             |
| [Ultimate Animation Pack](https://gitgud.io/Teacher/UAP)                                            | `214203` | 完整                         |
| [ElToros Bestiality Animations](https://gitgud.io/ElToro/rjw-elt-anim)                              | `1fa0fc` | 完整                         |
| [Privacy, Please!](https://gitgud.io/FireSplitter/privacy-please)                                   | `518778` | 完整                         |
| [RimJobWorld - Brothel Colony](https://gitgud.io/CalamaBanana/rjw-brothel-colony)                   | `211892` | 完整                         |
| [RimJobWorld - Milkable Colonists](https://gitgud.io/sombrahide/rjw-milkable-colonists-biotech)     | `4f7061` | 完整                         |
| [RJW-Events](https://gitgud.io/LukeLu/rjw-events)                                                   | `1f3832` | 完整                         |
| [ElToros Bestiality Addon](https://gitgud.io/ElToro/rjw-elt-baddon)                                 | `60fffb` | 完整                         |

### 已損壞的模組

參閱 RJW Wiki 附加模組列表，不提供更新與修正。

| 模組                                                                       | 版本     | 狀態 |
| -------------------------------------------------------------------------- | -------- | ---- |
| [RimJobWorld - Interaction Addon](https://gitgud.io/Ed86/rjw-ia)           | `13b209` | 完整 |
| [C0ffeeRIA](https://gitgud.io/c0ffeeeeeeee/coffees-rjw-ideology-addons)    | `f13a1f` | 完整 |
| [RimJobWorld - Licentia Labs](https://gitgud.io/Jaaldabaoth/licentia-labs) | `938d07` | 完整 |

# 參閱

- [RimWorld 官方社群繁體中文化](https://github.com/Ludeon/RimWorld-ChineseTraditional)
- [RJW Wiki](https://rjw.miraheze.org/wiki/Main_Page)
- [RJW Wiki 附加模組列表](https://rjw.miraheze.org/wiki/RJW_Add-On_List)
- [RJW Discord](https://discord.gg/CXwHhv8)
- [RJW Loverslab](https://www.loverslab.com/topic/110270-mod-rimjobworld)
- [RJW 巴哈討論串](https://forum.gamer.com.tw/C.php?bsn=27313&snA=812)

<details>
<summary></summary>

# 標準化

Simple is better.

❌ `crlf`<br />
✅ `lf`

❌ `utf-8-bom`<br />
✅ `utf-8`

```sh
find . -name "*.xml" | xargs dos2unix
```

</details>
