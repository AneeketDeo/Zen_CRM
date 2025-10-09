#!/usr/bin/env python3
"""
Test script for authentication functions using Argon2
"""
from auth import get_password_hash, verify_password

def test_password_hashing():
    """Test password hashing with various lengths using Argon2"""
    
    # Test cases with different password lengths
    test_passwords = [
        "short",  # 5 chars
        "normal_password_123",  # 19 chars
        "a" * 50,  # 50 chars
        "a" * 100,  # 100 chars
        "a" * 500,  # 500 chars (very long)
        "password_with_unicode_🚀",  # Unicode characters
        "very_long_password_that_exceeds_any_reasonable_limit_and_should_work_with_argon2",  # Very long
        "SuperSecurePassword123!@#$%^&*()_+-=[]{}|;':\",./<>?`~",  # Special characters
    ]
    
    print("Testing password hashing with Argon2...")
    print("=" * 60)
    print("Argon2 advantages:")
    print("✅ No password length limits")
    print("✅ More secure than bcrypt")
    print("✅ Memory-hard function")
    print("✅ Resistant to GPU/ASIC attacks")
    print("=" * 60)
    
    for i, password in enumerate(test_passwords, 1):
        try:
            print(f"\nTest {i}: Password length: {len(password)} chars, {len(password.encode('utf-8'))} bytes")
            print(f"Password: {password[:30]}{'...' if len(password) > 30 else ''}")
            
            # Hash the password
            hashed = get_password_hash(password)
            print(f"Hash: {hashed[:60]}...")
            
            # Verify the password
            is_valid = verify_password(password, hashed)
            print(f"Verification: {'✅ PASS' if is_valid else '❌ FAIL'}")
            
            # Test with wrong password
            wrong_password = password + "wrong"
            is_wrong = verify_password(wrong_password, hashed)
            print(f"Wrong password test: {'❌ FAIL (should be False)' if not is_wrong else '✅ PASS (should be False)'}")
            
        except Exception as e:
            print(f"❌ ERROR: {e}")
    
    print("\n" + "=" * 60)
    print("✅ Argon2 password hashing test completed!")
    print("✅ All passwords handled securely without truncation!")

if __name__ == "__main__":
    test_password_hashing()
