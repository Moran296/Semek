# Semek

![](https://github.com/Moran296/Semek/blob/master/semek.gif)

לפעמים כותבים בבאש משהו בלי להסתכל על המקלדת, ובעצם היינו בעברית,
באסה אה?
אז סעמק לוקח את הפקודה האחרונה שרצה, מתרגם לאנגלית כל אות ושולח שוב
קצת כמו thefuck הידוע

רק צריך לעשות קלון ואז לשים בbashrc את השורות הבאות:

```
alias סעמק='semek'
alias קמעס='semek'
export SEMEK_PATH='PATH/TO/Semek'
semek() {
    python $SEMEK_PATH/semek.py $(fc -ln -1)
    $(python $SEMEK_PATH/semek.py $(fc -ln -1))
}
```

וכמובן להחליף את הPATH/TO בנתיב הנכון,

בהצלחה


