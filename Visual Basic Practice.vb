Private sub BtnTax_Click()   
	Dim Salary(10) as Double
	Dim Location(10) As String
	Location(9) = "Nottingham"
	Location(7) = "France"
	
Print Location(9)
Print Location(7)

Salary(2) = 2003

end Sub

Dim myCollection As New Collection
Dim studentName As String, i as integer
Private Sub Command1_Click()
myCollection.Add(text1.text)
text1.text= ""
End Sub

Private Sub Command2_Click()
For i = i to my myCollection.Count
studentName = myCollection.Item(i)
MsqBox(studentName)
End Sub

Private Sub Commance3_Click()
MsqBox(myCollection.Count)
End Sub

Private Sun Text1_Change()
Dim day As Integer
day= val(Text1.text)

If day = 1 Then
	Text2.text = "Monday"
	
ElseIf day = 2 Then
	Text2.text = "Tuesday"
	
ElseIf day = 3 Then
	Text2.text = "Wednesday"
	
Else
	Text2.text = " Try entering a value equaling less than 7"
	
End If
End Sub


Private Sub Command1_Click()
Dim physics_mark As Integer, maths_mark As Integer
Dim english_mark As Integer, average As Integer
Dim result As String
physics_mark = Val(Text3.text)
maths_mark = Val(Text2.text)
english_mark = Val(Text1.text)

average = (physics_mark + maths_mark + english_mark)/3

Select case average
	Case Is <=50:
	
	Text4.text = "You Passed!"
	
	Case Is <=70:

	Text4.text = "Good Mark"
	
	Case Is <=90:
	
	Text4.text = "Top Student"
	
	Case is < 100:
	
	Text4.text = "Exceptional"
	
	Case Else
	
	Text4.text = " Sorry you failed"
	
End Select
End Sub

