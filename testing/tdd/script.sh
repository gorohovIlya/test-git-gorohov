grep import src/service.py | awk '{print $2}' > output.txt
sort -o output.txt output.txt
sort -o requirements.txt requirements.txt
diff -u output.txt requirements.txt | sed '1,2d' | grep "^[+-]" > final.txt
echo "missing libraries:"
grep "+" final.txt | sed 's/^+//'
echo "extra libraries:"
grep "-" final.txt | sed 's/^-//'
rm final.txt
rm output.txt
