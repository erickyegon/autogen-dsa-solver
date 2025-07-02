#!/usr/bin/env python3
"""
Test script to verify real AI collaboration is working
Run this before your YouTube recording to ensure everything works
"""

import asyncio
import os
import sys

# Add current directory to path
sys.path.append(os.path.dirname(__file__))

async def test_real_ai_collaboration():
    """Test if the real AutoGen team collaboration works"""
    
    print("🧪 Testing Real AI Collaboration...")
    print("=" * 50)
    
    # Test 1: Check API configuration
    print("\n1. 🔑 Checking API Configuration...")
    
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key:
        print(f"   ✅ OpenAI API key found (length: {len(api_key)})")
    else:
        print("   ❌ OpenAI API key not found!")
        print("   💡 Set it with: export OPENAI_API_KEY='your-key-here'")
        return False
    
    # Test 2: Import dependencies
    print("\n2. 📦 Testing Dependencies...")
    
    try:
        from main import get_enhanced_team_and_docker
        print("   ✅ Main module imported successfully")
    except Exception as e:
        print(f"   ❌ Main module import failed: {e}")
        return False
    
    try:
        from config.docker_utils import start_docker_executor, stop_docker_executor
        print("   ✅ Docker utils imported successfully")
    except Exception as e:
        print(f"   ❌ Docker utils import failed: {e}")
        return False
    
    # Test 3: Create team
    print("\n3. 🤖 Testing Team Creation...")
    
    try:
        team, docker = await get_enhanced_team_and_docker("scheduling", "medium")
        if team and docker:
            print("   ✅ Enhanced team created successfully!")
            print(f"   📊 Team type: {type(team).__name__}")
            print(f"   🐳 Docker type: {type(docker).__name__}")
        else:
            print("   ❌ Team or docker is None")
            return False
    except Exception as e:
        print(f"   ❌ Team creation failed: {e}")
        return False
    
    # Test 4: Simple collaboration test
    print("\n4. 🧠 Testing AI Collaboration...")
    
    try:
        test_problem = """
        Simple test: Find the maximum element in an array of integers.
        Provide a Python solution with O(n) time complexity.
        """
        
        print("   🚀 Starting AI collaboration test...")
        
        # Start Docker
        await start_docker_executor(docker)
        print("   ✅ Docker started")
        
        # Test team collaboration (just first few messages)
        message_count = 0
        async for message in team.run_stream(task=test_problem):
            message_count += 1
            print(f"   📝 Message {message_count}: {type(message).__name__}")
            
            # Stop after a few messages to avoid long test
            if message_count >= 3:
                break
        
        # Stop Docker
        await stop_docker_executor(docker)
        print("   ✅ Docker stopped")
        
        print(f"   ✅ AI collaboration test successful! ({message_count} messages)")
        
    except Exception as e:
        print(f"   ❌ AI collaboration test failed: {e}")
        return False
    
    print("\n🎉 ALL TESTS PASSED!")
    print("✅ Real AI collaboration is working!")
    print("🎬 Ready for YouTube recording!")
    
    return True

async def test_streamlit_integration():
    """Test if Streamlit integration works"""
    
    print("\n🌐 Testing Streamlit Integration...")
    
    try:
        import streamlit as st
        print("   ✅ Streamlit imported successfully")
        
        # Test if app.py can be imported
        import app
        print("   ✅ App module imported successfully")
        
        print("   💡 To test Streamlit app, run: streamlit run app.py")
        
    except Exception as e:
        print(f"   ❌ Streamlit integration test failed: {e}")
        return False
    
    return True

if __name__ == "__main__":
    print("🚀 DSA Solver Real AI Test Suite")
    print("=" * 50)
    
    # Run tests
    try:
        # Test real AI collaboration
        ai_success = asyncio.run(test_real_ai_collaboration())
        
        # Test Streamlit integration
        streamlit_success = asyncio.run(test_streamlit_integration())
        
        if ai_success and streamlit_success:
            print("\n🎉 SYSTEM READY FOR YOUTUBE RECORDING!")
            print("🎬 All components working correctly!")
            print("\n📋 Next steps:")
            print("1. Run: streamlit run app.py")
            print("2. Test with complex problems")
            print("3. Start recording!")
        else:
            print("\n⚠️ Some tests failed. Please fix issues before recording.")
            
    except KeyboardInterrupt:
        print("\n⏹️ Test interrupted by user")
    except Exception as e:
        print(f"\n❌ Test suite failed: {e}")
