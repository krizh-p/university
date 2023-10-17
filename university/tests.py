from django.test import Client, TestCase
from .models import Student, Course, Enrollment

class EnrollmentTestCase(TestCase):
    def setUp(self):
        # Create some test data
        self.student = Student.objects.create(
            first_name="John",
            last_name="Smith",
            gnum="0131"
        )

        self.course = Course.objects.create(
            title="Introduction to Programming",
            crn="CS110"
        )

    def test_valid_enrollment(self):
        """# Test a valid enrollment"""
        enrollment = Enrollment(student=self.student, course=self.course)

        # Check if the enrollment is valid
        self.assertTrue(enrollment.isValidEnrollment())

    def test_duplicate_enrollment(self):
        """# Test an invalid enrollment (duplicate)"""
        enrollment1 = Enrollment(student=self.student, course=self.course)
        enrollment1.save()

        enrollment2 = Enrollment(student=self.student, course=self.course)

        # Check if the second enrollment is not valid
        self.assertFalse(enrollment2.isValidEnrollment())

    def test_multiple_enrollments(self):
        """
        # Test multiple enrollments for the same student in different courses
        """
        course2 = Course.objects.create(
            title="Database Management",
            crn="CS550"
        )

        enrollment1 = Enrollment(student=self.student, course=self.course)

        enrollment2 = Enrollment(student=self.student, course=course2)

        # Check if both enrollments are valid
        self.assertTrue(enrollment1.isValidEnrollment())
        self.assertTrue(enrollment2.isValidEnrollment())

    def test_different_students_enrollment(self):
        """
         Test enrollments for different students in the same course
        """
        student2 = Student.objects.create(
            first_name="Alice",
            last_name="Johnson",
            gnum="0122"
        )

        enrollment1 = Enrollment(student=self.student, course=self.course)

        enrollment2 = Enrollment(student=student2, course=self.course)

        # Check if both enrollments are valid
        self.assertTrue(enrollment1.isValidEnrollment())
        self.assertTrue(enrollment2.isValidEnrollment())

    def test_index(self):
        c = Client()
        response = c.get("/university/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["students"].count(), 1)

    def test_invalid_page(self):
        c = Client()
        response = c.get("/gmu/")
        self.assertEqual(response.status_code, 404)